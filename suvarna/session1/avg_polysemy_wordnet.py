##Assignment5 - The polysemy of a word is the number of senses it has. Using WordNet, we can determine that the noun dog has 7 senses with: len(wn.synsets('dog', 'n')).
##Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.
import nltk
from nltk.corpus import wordnet as wn

poly_nouns = list(wn.all_synsets('n'))
poly_adjectives = list(wn.all_synsets(wn.ADJ))
poly_verbs = list(wn.all_synsets('v'))
poly_adverbs = list(wn.all_synsets(wn.ADV))


def calc_words(synset):
	all_words = []
	for syn in synset:
		all_words += syn.lemma_names()
	# eliminates duplicates and gets the count
	total = len(set(all_words))
	return total

def total_senses(synset):
	senses = sum(1 for x in synset)
	return senses

def avg_senses(synset):
    avg = total_senses(synset) / calc_words(synset)
    return avg

#print(total_senses(poly_nouns))
#print(calc_words(poly_nouns))
#print(calc_words(poly_nouns))
#print(calc_words(poly_nouns))

print("avg polysemy for noun",avg_senses(poly_nouns))
print("avg polysemy for adjectives",avg_senses(poly_adjectives))
print("avg polysemy for verb",avg_senses(poly_verbs))
print("avg polysemy for adverb",avg_senses(poly_adverbs))
