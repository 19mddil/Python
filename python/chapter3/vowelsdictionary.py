word = input("Give a word to search for vowels:")
vowels = "aeiou"#we could have written it like this vowels=['a','e','i','o','u']
found = {}
for letter in word:
	if letter in vowels:
		if letter not in found:
			found[letter] = 1
		else:
			found[letter] += 1
for k,v in sorted(found.items()):
	print(k,':',v)