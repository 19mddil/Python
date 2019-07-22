def s4v(phrase:str,letter:str) ->set:
	"""Return any specified letter in a word if exists so"""
	return set(letter).intersection(set(phrase))
print(s4v('lov','aeiou'))
