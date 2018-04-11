from nltk.corpus import wordnet as wn
synsetsWithNoHyponyms = len(set([s for s in wn.all_synsets('n') if len(s.hyponyms())==0]))
totalSynsets = len(set(wn.all_synsets('n')))
print("Synsets with No Hyponyms: ", synsetsWithNoHyponyms)
print("Total # synsets:", totalSynsets)
print("Percentage of synsets with no hyponymns:", synsetsWithNoHyponyms/totalSynsets*100 )


'''
Synsets with No Hyponyms:  65422
Total # synsets: 82115
Percentage of synsets with no hyponymns: 79.67119283931072
'''