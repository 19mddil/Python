#it also includes a sentence too(the input)....
word = input("Give a word to search for vowels:")
vowels = "aeiou"#we could have written it like this vowels=['a','e','i','o','u']
found = []
for letter in word:
	if letter in vowels:
		if letter not in found:
			found.append(letter)
for vowel in found:
	print(vowel)