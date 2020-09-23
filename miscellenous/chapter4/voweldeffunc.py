def s4v(word:str) ->set:
	#x = """\twhat the fuck am I doing
    #\tnow lets see"""
	#print(x)
	"""returns vowels in a word"""
	vowels = "aeiou"#we could have written it like this vowels=['a','e','i','o','u']
	vowel = set(vowels)
	return vowel.intersection(set(word))

print(s4v("sky"))
help(s4v)