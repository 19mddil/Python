word = input("Give a word to search for vowels:")
vowels = "aeiou"#we could have written it like this vowels=['a','e','i','o','u']
vowel = set(vowels)
sword = vowel.intersection(set(word))