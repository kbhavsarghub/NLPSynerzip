from nltk.corpus import brown
import nltk
humorTokens = brown.words(categories = ['humor'])
print("Token Count in Humor:", len(humorTokens))
print("Type Count of Words in Humor:", len(set(humorTokens)))
print("Lexical Diversity Score:", len(humorTokens)/len(set(humorTokens)))

romanceTokens = brown.words(categories = ['romance'])
print("Token Count in romance:", len(romanceTokens))
print("Type Count of Words in romance:", len(set(romanceTokens)))
print("Lexical Diversity Score:", len(romanceTokens)/len(set(romanceTokens)))

'''
Token Count in Humor: 21695
Type Count of Words in Humor: 5017
Lexical Diversity Score: 4.324297388877816
---------------------------------------------
Token Count in romance: 70022
Type Count of Words in romance: 8452
Lexical Diversity Score: 8.284666351159489
----------------------------------------------
'''