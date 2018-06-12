
amino_acids = ['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']

charged = ['K','R','D','E']
pos =['K','R']
neg =['D','E']
polar = ['Q','N','H','S','T','Y','C','M','W']
hydrophobic = ['A','I','L','F','V','P','G']

categories = ['P_P','H_H','CP_CP','CN_CN','P_H','P_CP','P_CN','H_P','H_CP','H_CN','CP_P','CP_H','CP_CN','CN_P','CN_H','CN_CP']

def convert_cat_code(cat):
    if cat == 'P_P':
        return 'Polar to Polar'
    elif cat == 'H_H':
        return 'Hydrophobic to Hydrophobic'
    elif cat == 'CP_CP':
        return 'Charged-Positive to Charged-Positive'
    elif cat == 'CN_CN':
        return 'Charged-Negative to Charged-Negative'
    elif cat == 'P_H':
        return 'Polar to Hydrophobic'
    elif cat == 'P_CP':
        return 'Polar to Charged-Positive'
    elif cat == 'P_CN':
        return 'Polar to Charged-Negative'
    elif cat == 'H_P':
        return 'Hydrophobic to Polar'
    elif cat == 'H_CP':
        return 'Hydrophobic to Charged-Positive'
    elif cat == 'H_CN':
        return 'Hydrophobic to Charged-Negative'
    elif cat == 'CP_P':
        return 'Charged-Positive to Polar'
    elif cat == 'CP_H':
        return 'Charged-Positive to Hydrophobic'
    elif cat == 'CP_CN':
        return 'Charged-Positive to Charged-Negative'
    elif cat == 'CN_P':
        return 'Charged-Negative to Polar'
    elif cat == 'CN_H':
        return 'Charged-Negative to Hydrophobic'
    elif cat == 'CN_CP':
        return 'Charged-Negative to Charged-Positive'






PR_Mutations = """[ "PR:L10ARNDCEQGHILKMFPSTWYV",
                    "PR:V11ARNDCEQGHILKMFPSTWYV",
                    "PR:I13ARNDCEQGHILKMFPSTWYV",
                    "PR:K20ARNDCEQGHILKMFPSTWYV",
                    "PR:L23ARNDCEQGHILKMFPSTWYV",
                    "PR:L24ARNDCEQGHILKMFPSTWYV",
                    "PR:D30ARNDCEQGHILKMFPSTWYV",
                    "PR:V32ARNDCEQGHILKMFPSTWYV",
                    "PR:L33ARNDCEQGHILKMFPSTWYV",
                    "PR:E35ARNDCEQGHILKMFPSTWYV",
                    "PR:M36ARNDCEQGHILKMFPSTWYV",
                    "PR:K43ARNDCEQGHILKMFPSTWYV",
                    "PR:M46ARNDCEQGHILKMFPSTWYV",
                    "PR:I47ARNDCEQGHILKMFPSTWYV",
                    "PR:G48ARNDCEQGHILKMFPSTWYV",
                    "PR:I50ARNDCEQGHILKMFPSTWYV",
                    "PR:F53ARNDCEQGHILKMFPSTWYV",
                    "PR:I54ARNDCEQGHILKMFPSTWYV",
                    "PR:Q58ARNDCEQGHILKMFPSTWYV",
                    "PR:L63ARNDCEQGHILKMFPSTWYV",
                    "PR:A71ARNDCEQGHILKMFPSTWYV",
                    "PR:G73ARNDCEQGHILKMFPSTWYV"
                    "PR:T74ARNDCEQGHILKMFPSTWYV",
                    "PR:L76ARNDCEQGHILKMFPSTWYV",
                    "PR:V77ARNDCEQGHILKMFPSTWYV",
                    "PR:V82ARNDCEQGHILKMFPSTWYV",
                    "PR:N83ARNDCEQGHILKMFPSTWYV",
                    "PR:I84ARNDCEQGHILKMFPSTWYV",
                    "PR:I85ARNDCEQGHILKMFPSTWYV",
                    "PR:N88ARNDCEQGHILKMFPSTWYV",
                    "PR:L89ARNDCEQGHILKMFPSTWYV",
                    "PR:L90ARNDCEQGHILKMFPSTWYV",
                    "PR:I93ARNDCEQGHILKMFPSTWYV"
                  ]"""

IN_Mutations = """[ "IN:H51ARNDCEQGHILKMFPSTWYV",
                    "IN:T66ARNDCEQGHILKMFPSTWYV",
                    "IN:L74ARNDCEQGHILKMFPSTWYV",
                    "IN:E92ARNDCEQGHILKMFPSTWYV",
                    "IN:Q95ARNDCEQGHILKMFPSTWYV",
                    "IN:T97ARNDCEQGHILKMFPSTWYV",
                    "IN:H114ARNDCEQGHILKMFPSTWYV",
                    "IN:F121ARNDCEQGHILKMFPSTWYV",
                    "IN:A128ARNDCEQGHILKMFPSTWYV",
                    "IN:E138ARNDCEQGHILKMFPSTWYV",
                    "IN:G140ARNDCEQGHILKMFPSTWYV",
                    "IN:Y143ARNDCEQGHILKMFPSTWYV",
                    "IN:P145ARNDCEQGHILKMFPSTWYV",
                    "IN:Q146ARNDCEQGHILKMFPSTWYV",
                    "IN:S147ARNDCEQGHILKMFPSTWYV",
                    "IN:Q148ARNDCEQGHILKMFPSTWYV",
                    "IN:V151ARNDCEQGHILKMFPSTWYV",
                    "IN:S153ARNDCEQGHILKMFPSTWYV",
                    "IN:N155ARNDCEQGHILKMFPSTWYV",
                    "IN:E157ARNDCEQGHILKMFPSTWYV",
                    "IN:G163ARNDCEQGHILKMFPSTWYV",
                    "IN:S230ARNDCEQGHILKMFPSTWYV",
                    "IN:R263ARNDCEQGHILKMFPSTWYV"
               ]"""

RT_Mutations = """[ "RT:E40ARNDCEQGHILKMFPSTWYV",
                    "RT:M41ARNDCEQGHILKMFPSTWYV",
                    "RT:E44ARNDCEQGHILKMFPSTWYV",
                    "RT:A62ARNDCEQGHILKMFPSTWYV",
                    "RT:K65ARNDCEQGHILKMFPSTWYV",
                    "RT:D67ARNDCEQGHILKMFPSTWYV",
                    "RT:T69ARNDCEQGHILKMFPSTWYV",
                    "RT:K70ARNDCEQGHILKMFPSTWYV",
                    "RT:L74ARNDCEQGHILKMFPSTWYV",
                    "RT:F77ARNDCEQGHILKMFPSTWYV",
                    "RT:V90ARNDCEQGHILKMFPSTWYV",
                    "RT:A98ARNDCEQGHILKMFPSTWYV",
                    "RT:L100ARNDCEQGHILKMFPSTWYV",
                    "RT:K101ARNDCEQGHILKMFPSTWYV",
                    "RT:K103ARNDCEQGHILKMFPSTWYV",
                    "RT:V106ARNDCEQGHILKMFPSTWYV",
                    "RT:V108ARNDCEQGHILKMFPSTWYV",
                    "RT:Y115ARNDCEQGHILKMFPSTWYV",
                    "RT:F116ARNDCEQGHILKMFPSTWYV",
                    "RT:V118ARNDCEQGHILKMFPSTWYV",
                    "RT:E138ARNDCEQGHILKMFPSTWYV",
                    "RT:Q151ARNDCEQGHILKMFPSTWYV",
                    "RT:V179ARNDCEQGHILKMFPSTWYV",
                    "RT:Y181ARNDCEQGHILKMFPSTWYV",
                    "RT:M184ARNDCEQGHILKMFPSTWYV",
                    "RT:Y188ARNDCEQGHILKMFPSTWYV",
                    "RT:G190ARNDCEQGHILKMFPSTWYV",
                    "RT:L210ARNDCEQGHILKMFPSTWYV",
                    "RT:T215ARNDCEQGHILKMFPSTWYV",
                    "RT:K219ARNDCEQGHILKMFPSTWYV",
                    "RT:H221ARNDCEQGHILKMFPSTWYV",
                    "RT:P225ARNDCEQGHILKMFPSTWYV",
                    "RT:F227ARNDCEQGHILKMFPSTWYV",
                    "RT:M230ARNDCEQGHILKMFPSTWYV",
                    "RT:P236ARNDCEQGHILKMFPSTWYV",
                    "RT:K238ARNDCEQGHILKMFPSTWYV",
                    "RT:Y318ARNDCEQGHILKMFPSTWYV",
                    "RT:N348ARNDCEQGHILKMFPSTWYV",
               ]"""

PR_query =  """ query {
                    viewer {
                        mutationsAnalysis(mutations: """+PR_Mutations+"""  ) {
                          drugResistance {
                            drugScores {
                              drug {
                                name
                              },
                               partialScores {
                                mutations {
                                  text
                                },
                                score
                              }
                            }
                          }
                        }
                    }
                 } """

IN_query ="""query {
                viewer {
                    mutationsAnalysis(mutations: """+IN_Mutations+""" ) {
                      drugResistance {
                        drugScores {
                          drug { name },
                          partialScores {
                            mutations {
                              text
                            },
                            score
                          }
                        },
                      }
                    }
                }
            } """


RT_query =  """ query {
                    viewer {
                        mutationsAnalysis(mutations: """+RT_Mutations+"""  ) {
                          drugResistance {
                            drugScores {
                              drug {
                                name
                              },
                               partialScores {
                                mutations {
                                  text
                                },
                                score
                              }
                            }
                          }
                        }
                    }
                 } """