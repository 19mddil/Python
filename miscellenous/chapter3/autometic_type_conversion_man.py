word = 'hello'#first was string object
vowels = 'aeiou'
word =set(vowels).intersection(set(word))#then becomes a set?????
#word = word.intersection(vowels)# results in a error as expected
#word = ''.join(word)#so  you can use join to convert in string for set and list both
print(word)
word = list(word)
print(word)
word = ''.join(word)
print(word)