#Accept a paragraph from user. Create a set of unique words. Display number of unique words and display common words between two sentences

para=input('Enter a paragraph here')
words=para.split()
print(words)
set_words=set(words)
print("No. of unique characters are ",len(set_words))
print(set_words)
