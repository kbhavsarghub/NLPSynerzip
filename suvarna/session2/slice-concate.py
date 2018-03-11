##1. Define a string s = 'colorless'. Write a Python statement that changes this to "colourless" using only the slice and concatenation operations
s = 'colorless'
s_two = ''
s_two = s[0:4] + 'u' + s[4:]
print(s_two)

## another way

wordList = s.split('r')
print((type(wordList)), ':', wordList)
names = 'ur'.join(wordList)
print(names)
