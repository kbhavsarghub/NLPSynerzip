#4. Calculate what percentage of words are stopwords in the reuters corpus
from nltk.corpus import reuters
from nltk.corpus import stopwords


stopWordsSize = len(set(stopwords.words()))
reutersSize = len(reuters.words())

print(round((stopWordsSize/reutersSize)*100 ,2),"%")