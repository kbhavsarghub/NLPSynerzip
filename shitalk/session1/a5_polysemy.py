from nltk.corpus import wordnet as wn

def polysemy(wordType):
    polysemy = 0        #No of senses
    count = 0
    for synset in wn.all_synsets(wordType):
        for lemma in synset.lemmas():
            name = lemma.name()
            polysemy = polysemy + len(wn.synsets(name, wordType))
            count = count + 1
    return polysemy / count

print ("Noun",polysemy('n'))
print ("Verb",polysemy('v'))
print ("Adverb",polysemy('r'))
print ("Adjective",polysemy('a'))

'''
Noun 1.8525012470361537
Verb 5.098255280073462
Adverb 1.6985663082437277
Adjective 2.233702173043594
'''