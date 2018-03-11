#4. Create a file consisting of words and (made up) frequencies,
# where each line consists of a word, the space character, and a positive integer,
# e.g. fuzzy 53. Read the file into a Python list using
# open(filename).readlines().
# Next, break each line into its two fields using split(), and convert the number into an integer using int().
#The result should be a list of the form: [['fuzzy', 53], ...

def load(name):
    file = open(name, 'r')
    text1 = file.read()
    return (text1)



text=load('word-freq.txt');
textList = text.split('\n')
print((type(textList)), ':', textList)
ln=[]
for s in textList:
    wordList = s.split(' ')
    wordList[1]=int(wordList[1])
    ln.append(wordList)
   

print('hi')
print(ln)

