##Assignment6 - What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n')
import nltk
from nltk.corpus import wordnet as wn

nb_syn = sum(1 for _ in wn.all_synsets('n'))
fac = len([s for s in wn.all_synsets('n') if len(s.hyponyms()) == 0]) / nb_syn
print ("The percentage of noun synsets with no hyponyms is %f" % fac)