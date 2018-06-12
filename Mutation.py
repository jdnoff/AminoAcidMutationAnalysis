
class MultipleMutant:
    def __init__(self,mutations,resistance):
        self.mutations = mutations
        self.resistances = []
        self.resistances.append(resistance)

    def add_mult_score(self,score):
        self.resistances.append(score)

class AminoAcid:
    def __init__(self,name, avgRes=0):
        self.name = name
        self.avg_res = avgRes
        self.impact = 0
        self.impact_to_overall = 0
        self.impact_by_cat = 0

    def set_impact(self, impact):
        self.impact = impact

    def print_avg(self):
        print(self.name+":",self.avg_res)

    def print_impact(self):
        print(self.name + ":", self.impact)

class MutationList:
    def __init__(self):
        self.mutations = []
        self.multimutants = []

    def add_mutation(self, mutation):
        self.mutations.append(mutation)

    def add_multimutant(self,multimutant):
        self.multimutants.append(multimutant)

    def get_names(self):
        names = []
        for mutation in self.mutations:
            names.append(mutation.get_name())
        return names

    def add_score(self, name, score):
        for mutation in self.mutations:
            if name == mutation.get_name():
                mutation.add_score(score)

    def add_multi_score(self, names, score):
        for mutation in self.multimutants:
            if names == mutation.mutations:
                mutation.add_score(score)

    def print_ml(self):
        for mutation in self.mutations:
            print(mutation.name,mutation.scores)

    def print_avgs(self):
        for mutation in self.mutations:
            print(mutation.name+':',mutation.avg_score)

    def fill_blanks(self):
        for mutation in self.mutations:
            mutation.fill_blanks()

    def get_averages(self):
        for mutation in self.mutations:
            mutation.avg_res()

class Mutation:
    def __init__(self, mutation, type, score):
        self.name = mutation
        self.type = type
        if type == 1:
            self.drugCount = 8
        elif type == 2:
            self.drugCount = 3
        elif type == 3:
            self.drugCount = 11
        self.scores = []
        self.scores.append(score)
        self.avg_score = 0
        self.impact = 0

    def add_score(self, score):
        self.scores.append(score)

    def fill_blanks(self):
        if len(self.scores) < self.drugCount:
            for score in range(0,self.drugCount-len(self.scores)):
                self.add_score(0)

    def avg_res(self):
        self.avg_score = sum(self.scores)/float(len(self.scores))

    def get_name(self):
        return self.name

    def setCategory(self,start,end):
        self.category = start + '_' + end

