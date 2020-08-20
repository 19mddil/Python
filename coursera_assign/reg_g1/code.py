import re
hand = open('regex_sum_908090.txt')
long_string = hand.read()
numlist = re.findall('[0-9]+',long_string)
print(sum([int(s) for s in numlist]))
