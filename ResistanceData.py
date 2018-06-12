
from Constants import *
from Mutation import AminoAcid

class Category:
    def __init__(self,name,mutations):
        self.name = name
        self.mutations = mutations
        self.set = self.get_set()
        self.amino_acids = self.score_amino_acids()


    def score_amino_acids(self):
        aminos = []
        for aa in self.set:
            acid = AminoAcid(aa)
            mut_impacts = []
            for mutation in self.mutations:
                if mutation.name.endswith(aa):
                    mut_impacts.append(mutation.impact)
            if mut_impacts:
                acid.set_impact(round(sum(mut_impacts)/float(len(mut_impacts)),3))
                aminos.append(acid)
        return aminos

    def get_set(self):
        name = self.name.split('_')
        try:
            name = name[1]
        except:
            name = name[0]
        if name == 'P':
            return polar
        elif name == 'H':
            return hydrophobic
        elif name == 'CP':
            return pos
        elif name == 'CN':
            return neg

class ResistanceData:
    def __init__(self, allData, aa_data):
        self.aa_data = aa_data
        self.mutation_data = allData
        self.overall_avg = self.avg_mutation_res()

        self.test_categories()
        self.get_resistances()
        self.score_mutations()
        self.final_aa_scores = self.score_aa_final(aa_data)
        self.category_data = self.score_by_cat_final()

        self.polar_impact = self.polar_avg - self.overall_avg
        self.hydro_impact = self.hydro_avg - self.overall_avg
        self.pos_impact = self.pos_avg - self.overall_avg
        self.neg_impact = self.neg_avg - self.overall_avg


    def test_categories(self):
        polar_scores= 0
        hydro_scores = 0
        pos_scores = 0
        neg_scores = 0
        for aa in self.aa_data:
            if aa.name in polar:
                polar_scores += aa.avg_res
            elif aa.name in hydrophobic:
                hydro_scores += aa.avg_res
            elif aa.name in pos:
                pos_scores += aa.avg_res
            elif aa.name in neg:
                neg_scores += aa.avg_res
        self.polar_avg = polar_scores / float(len(polar))
        self.hydro_avg = hydro_scores / float(len(hydrophobic))
        self.pos_avg = pos_scores / float(len(pos))
        self.neg_avg = neg_scores / float(len(neg))

    def avg_mutation_res(self):
        avg = 0
        count = 0
        for data in self.mutation_data:
            for mutation in data.mutations:
                count += 1
                avg += mutation.avg_score
        return avg / float(count)

    def get_category(self,amino_acid):
        if amino_acid in polar:
            return 'P'
        elif amino_acid in hydrophobic:
            return 'H'
        elif amino_acid in pos:
            return 'CP'
        elif amino_acid in neg:
            return 'CN'

    def test_interCategory(self, startCat, endCat):
        mutList = []
        for data in self.mutation_data:
            for mutation in data.mutations:
                for amino in startCat:
                    for acid in endCat:
                        if mutation.name.startswith(amino) and mutation.name.endswith(acid):
                            mutation.setCategory(self.get_category(amino), self.get_category(acid))
                            mutList.append(mutation.avg_score)
        return sum(mutList) / float(len(mutList))

    def get_resistances(self):
        self.polar_polar = self.test_interCategory(polar, polar)
        self.hydro_hydro = self.test_interCategory(hydrophobic, hydrophobic)
        self.pos_pos = self.test_interCategory(pos, pos)
        self.neg_neg = self.test_interCategory(neg, neg)

        self.polar_hydro = self.test_interCategory(polar, hydrophobic)
        self.polar_pos = self.test_interCategory(polar, pos)
        self.polar_neg = self.test_interCategory(polar, neg)

        self.hydro_polar = self.test_interCategory(hydrophobic, polar)
        self.hydro_pos = self.test_interCategory(hydrophobic, pos)
        self.hydro_neg = self.test_interCategory(hydrophobic, neg)

        self.pos_polar = self.test_interCategory(pos, polar)
        self.pos_hydro = self.test_interCategory(pos, hydrophobic)
        self.pos_neg = self.test_interCategory(pos, neg)

        self.neg_polar = self.test_interCategory(neg, polar)
        self.neg_hydro = self.test_interCategory(neg, hydrophobic)
        self.neg_pos = self.test_interCategory(neg, pos)

    def get_cat_avg(self, cat):
        cat = cat.split('_')
        cat = cat[1]
        if cat == 'P':
            return self.polar_avg
        elif cat == 'H':
            return self.hydro_avg
        elif cat == 'CP':
            return self.pos_avg
        elif cat == 'CN':
            return self.neg_avg

    def get_cat_cat_avg(self, cat):
        if cat == 'P_P':
            return self.polar_polar
        elif cat == 'H_H':
            return self.hydro_hydro
        elif cat == 'CP_CP':
            return self.pos_pos
        elif cat == 'CN_CN':
            return self.neg_neg
        elif cat == 'P_H':
            return self.polar_hydro
        elif cat == 'P_CP':
            return self.polar_pos
        elif cat == 'P_CN':
            return self.polar_neg
        elif cat == 'H_P':
            return self.hydro_polar
        elif cat == 'H_CP':
            return self.hydro_pos
        elif cat == 'H_CN':
            return self.hydro_neg
        elif cat == 'CP_P':
            return self.pos_polar
        elif cat == 'CP_H':
            return self.pos_hydro
        elif cat == 'CP_CN':
            return self.pos_neg
        elif cat == 'CN_P':
            return self.neg_polar
        elif cat == 'CN_H':
            return self.neg_hydro
        elif cat == 'CN_CP':
            return self.neg_pos

    def score_mutations(self):
        for data in self.mutation_data:
            for mutation in data.mutations:
                cat_cat_avg = self.get_cat_cat_avg(mutation.category)
                cat_avg = self.get_cat_avg(mutation.category)
                mutation.impact = mutation.avg_score - cat_cat_avg
                mutation.impact_to_overall = mutation.avg_score - self.overall_avg
                mutation.impact_by_cat = mutation.avg_score - cat_avg

    def score_aa_final(self, amino_acid_data):
        aaList = []
        for aa in amino_acid_data:
            impacts_to_overall = []
            impacts_by_cat = []
            for data in self.mutation_data:
                for mutation in data.mutations:
                    if mutation.name.endswith(aa.name):
                        impacts_to_overall.append(mutation.impact_to_overall)
                        impacts_by_cat.append(mutation.impact_by_cat)
            aa.impact_to_overall = sum(impacts_to_overall) / float(len(impacts_to_overall))
            aa.impact_by_cat = sum(impacts_by_cat) / float(len(impacts_by_cat))
            aaList.append(aa)
            aaList.sort(key=lambda aa: aa.impact_to_overall)
        return aaList

    def score_by_cat_final(self):
        cats = []
        for cat in categories:
            muts = []
            for data in self.mutation_data:
                for mutation in data.mutations:
                    if mutation.category == cat:
                        muts.append(mutation)
            cats.append(Category(cat,muts))
        return cats
