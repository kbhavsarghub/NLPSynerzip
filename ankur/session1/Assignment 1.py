# 1. Compare lexical diversity scores of humor, fiction and romance in brown corpus. Find out which genre is more lexically diverse?
from nltk.corpus import brown
from nltk.text import Text
from operator import itemgetter

genres = ['fiction', 'humor', 'romance']

print("Lexical Diversity :")

LD = {}
for genre in genres:
    currentWords = Text(brown.words(categories=[genre]))
    LD[genre.title()] = round(len(set(currentWords)) / len(currentWords) * 100, 2)

for k,v in sorted(LD.items(), key=itemgetter(1) , reverse=True):
    print(k,v)



