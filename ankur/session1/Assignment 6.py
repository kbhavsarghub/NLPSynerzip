#6. What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n')
from nltk.corpus import wordnet as wn

nounSynsets = set(wn.all_synsets('n'))

zeroCount=0
total=0
for synset in nounSynsets:
    total += 1
    if len(synset.hyponyms()) == 0:
        zeroCount += 1

percentage = round( (zeroCount / total) * 100, 2)
print(percentage,"%")


