#3. Save some text into a file corpus.txt. Define a function load(f) that reads from the file named in its sole argument,
# and returns a string containing the text of the file

def load(name):
    file = open(name, 'r')
    text1 = file.read()
    return (text1)



print(load('corpus.txt'))