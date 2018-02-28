from nltk.corpus import reuters,stopwords
import nltk
stopwordCount = len([w for w in reuters.words() if w in stopwords.words('english')])
wordCount = len[reuters.words()]

print("Stopword count in reuters:",stopwordCount)
print("Total wordcount in reuters:", wordCount)
print("Percentage of stopwords:", stopwordCount/wordCount*100)

