lowercase_alph = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
for a in lowercase_alph:
  for b in lowercase_alph:
    for c in numbers:
      for d in numbers:
        print(a+b+c+d) #generating all possible 4 digit passwords starting with two characters
#list comprehension
for password in [a+b+c+d for a in lowercase_alph for b in lowercase_alph for c in numbers for d in numbers]: print(numbers)
