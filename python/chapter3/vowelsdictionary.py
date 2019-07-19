word = input("Give a word to search for vowels:")
vowels = "aeiou"#we could have written it like this vowels=['a','e','i','o','u']
found = {'e':0,'i':0,'u':0,'o':0,'a':0}
for letter in word:
	if letter in vowels:
		found[letter] += 1
		print(found[letter])
for k,v in sorted(found.items()):
	print(k,':',v)