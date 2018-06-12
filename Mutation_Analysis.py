# script which gets mutations & their resistance scores from HIVdb
# stores results as a csv file.

from gql import gql
from sierrapy import SierraClient
from Constants import *
from Mutation import *
from ResistanceData import *

def printData(data):
    for drug in data['viewer']['mutationsAnalysis']['drugResistance'][0]['drugScores']:
        print(''+drug['drug']['name']+':')
        for mutations in drug['partialScores']:
            try:
                x = mutations['mutations'][1]['text']
                print("\t","Multiple Mutant - Omit")
            except:
                print("\t", mutations['mutations'][0]['text'], mutations['score'])

def compileMutations(data, type):
    mutationList = MutationList()
    for drug in data['viewer']['mutationsAnalysis']['drugResistance'][0]['drugScores']:
        for mutations in drug['partialScores']:
            try:
                x = mutations['mutations'][1]['text']
                muts = []
                for mutation in mutations['mutations']:
                    muts.append(mutation['text'])
                temp = mutations['mutations'][0]['text']
                mutationList.add_multimutant(MultipleMutant(muts,mutations['score']))

            except:
                temp = mutations['mutations'][0]['text']
                if temp not in mutationList.get_names():
                    newMutation = Mutation(temp, type, mutations['score'])
                    mutationList.add_mutation(newMutation)
                else:
                    mutationList.add_score(temp, mutations['score'])
    mutationList.fill_blanks()
    mutationList.get_averages()
    return mutationList

def compile_amino_acids(allData):
    aaList = []
    for aa in amino_acids:
        scores = []
        for data in allData:
            for mutation in data.mutations:
                if mutation.name.endswith(aa):
                    scores.append(mutation.avg_score)
                    #print('\t',mutation.name,mutation.avg_score)
        acid_score = sum(scores) / float(len(scores))
        aaList.append(AminoAcid(aa,acid_score))
    aaList.sort(key=lambda aa: aa.avg_res, reverse=True)
    return aaList

def dump_data(resistance_data, amino_acid_data):
    print("\nAverage Resistance for All Mutations:", resistance_data.overall_avg)

    print('\n----------Avg Overall Resistance by Category (Anything to Polar etc.)--------------\n')
    print('Polar Average: ', resistance_data.polar_avg)
    print('Hydrophobic Average: ', resistance_data.hydro_avg)
    print('Charged-Positive Average: ', resistance_data.pos_avg)
    print('Charged-Negative Average: ', resistance_data.neg_avg)

    print('\n----------Avg Resistance for Same Category Mutations (Polar to Polar etc.)---------\n')
    print("Polar to Polar: ", resistance_data.polar_polar)
    print("Hydrophobic to Hydrophobic: ", resistance_data.hydro_hydro)
    print("Charged-Positive to Charged-Positive: ", resistance_data.pos_pos)
    print("Charged-Negative to Charged-Negative: ", resistance_data.neg_neg)

    print('\n--------Avg Resistance for Inter-Category Mutations (Polar to Charged etc.)--------\n')
    print("Polar to Hydrophobic: ", resistance_data.polar_hydro)
    print("Polar to Charged-Positive: ", resistance_data.polar_pos)
    print("Polar to Charged-Negative: ", resistance_data.polar_neg, '\n')

    print("Hydrophobic to Polar: ", resistance_data.hydro_polar)
    print("Hydrophobic to Charged-Positive: ", resistance_data.hydro_pos)
    print("Hydrophobic to Charged-Negative: ", resistance_data.hydro_neg, '\n')

    print("Charged-Positive to Polar: ", resistance_data.pos_polar)
    print("Charged-Positive to Hydrophobic: ", resistance_data.pos_hydro)
    print("Charged-Positive to Charged-Negative: ", resistance_data.pos_neg, '\n')

    print("Charged-Negative to Polar: ", resistance_data.neg_polar)
    print("Charged-Negative to Hydrophobic: ", resistance_data.neg_hydro)
    print("Charged-Negative to Charged-Positive: ", resistance_data.neg_pos, '\n')

def dump_multiple_mutant_data(allData):
    total = 0
    count = 0
    for data in allData:
        for multimutation in data.multimutants:
            print(multimutation.mutations,multimutation.resistance)
            total += multimutation.resistance
            count += 1
    avg = total/float(count)
    print("\nMultiple Mutant Average Resistance: ",avg )

def dump_results(resistance_data):
    print("\n------------------Impact on Binding: Compared to Overall Average--------------------\n")
    print("Overall Average Resistance: ", resistance_data.overall_avg, '\n')
    for aa in resistance_data.final_aa_scores:
        print(aa.name + ":", aa.impact_to_overall)

    resistance_data.final_aa_scores.sort(key=lambda aa: aa.impact_by_cat)
    print("\n--------------Impact on Binding: Compared to Any -> Category Average-----------------\n")

    print("Any to Polar:\n\n","\t Average Resistance:",resistance_data.polar_avg)
    print("\t Polar Impact:",resistance_data.polar_impact,'\n')
    for aa in resistance_data.final_aa_scores:
        if aa.name in polar:
            print('\t', aa.name + ":", aa.impact_by_cat)

    print("\nAny to Hydrophobic:\n\n", "\t Average Resistance:", resistance_data.hydro_avg)
    print("\t Hydrophobic Impact:", resistance_data.hydro_impact, '\n')
    for aa in resistance_data.final_aa_scores:
        if aa.name in hydrophobic:
            print('\t', aa.name + ":", aa.impact_by_cat)

    print("\nAny to Charged-Positive:\n\n", "\t Average Resistance:", resistance_data.pos_avg)
    print("\t Charged-Positive Impact:", resistance_data.pos_impact, '\n')
    for aa in resistance_data.final_aa_scores:
        if aa.name in pos:
            print('\t', aa.name + ":", aa.impact_by_cat)

    print("\nAny to Charged-Negative:\n\n", "\t Average Resistance:", resistance_data.neg_avg)
    print("\t Charged-Negative Impact:", resistance_data.neg_impact, '\n')
    for aa in resistance_data.final_aa_scores:
        if aa.name in neg:
            print('\t', aa.name + ":",aa.impact_by_cat)

    print("\n-----------Impact on Binding: Compared to Category -> Category Average--------------")
    for cat in resistance_data.category_data:
        print('\n',convert_cat_code(cat.name) + ":\n")
        print('\t Average Resistance:',resistance_data.get_cat_cat_avg(cat.name),'\n')
        print('\t',convert_cat_code(cat.name),'Impact:',resistance_data.get_cat_cat_avg(cat.name)-resistance_data.overall_avg)
        for aa in cat.amino_acids:
            print('\t', aa.name + ":", aa.impact)

    print("\n-----------------------Category-Category Impact Data------------------------------\n")
    for cat in resistance_data.category_data:
        print('\t',convert_cat_code(cat.name), round(resistance_data.get_cat_cat_avg(cat.name) - resistance_data.overall_avg,3))


#Test Script
client = SierraClient('https://hivdb.stanford.edu/graphql')

PR_data = client.execute( gql(PR_query) )
PR_muts = compileMutations(PR_data,1)

IN_data = client.execute( gql(IN_query) )
IN_muts = compileMutations(IN_data,2)

RT_data = client.execute( gql(RT_query) )
RT_muts = compileMutations(RT_data,3)

allData = [PR_muts,IN_muts,RT_muts]

amino_acid_data = compile_amino_acids(allData)
resistance_data = ResistanceData(allData, amino_acid_data)

dump_data(resistance_data,amino_acid_data)
dump_results(resistance_data)

#dump_multiple_mutant_data(allData)
