from nltk.corpus import brown
import nltk


def getWHCount(categoryName):
    whList = ([w for w in brown.words(categories=[categoryName]) if w in ['who','where','how','what','whose','whom']])
    return len(whList)

print('WH words count in adventure:',getWHCount('adventure'))
print('WH words count in editorial:',getWHCount('editorial'))
print('WH words count in government:',getWHCount('government'))

'''
WH words count in adventure: 293
WH words count in editorial: 358
WH words count in government: 196
'''