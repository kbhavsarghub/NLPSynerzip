#3. Count all the wh(what, when, where, why, who, how etc.) words is any three different categories in Brown corpus
import nltk
from nltk.corpus import brown

genres = ['fiction', 'science_fiction', 'adventure']
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']


for genre in genres:
    print("WH words in '"+ genre.title() + "'")
    currentWords = brown.words(categories = genre)
    fdist = nltk.FreqDist(currentWords)
    total =0
    for wh in whwords:
        currentCount = fdist[wh]
        total+=currentCount
        print(wh + ':', currentCount, end=' ')
    print("\nTotal :",total,"\n")


