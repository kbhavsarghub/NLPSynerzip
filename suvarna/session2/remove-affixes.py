#2. Use slice notation to remove the affixes from these words
## (I've inserted a hyphen to indicate the affix boundary, but omit this from your strings)
## : dish-es, run-ning, nation-ality, un-do, pre-heat
str='dishes'
print('removing affixes from dishes:',str[:-2])
str='running'
print('removing affixes from running:',str[:-4])
str='nationality'
print('removing affixes from running:',str[:-5])
str='undo'
print('removing affixes from running:',str[:-2])
str='preheat'
print('removing affixes from running:',str[:-4])