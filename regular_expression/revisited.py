import re

text = 'Amy works diligently. Amy gets good grades. Our student Amy is successful.'
re.split('Amy',text) #splits the string using the pattern specified ['',' works diligently. ',' gets good grades. Our student ',' is successful.']
re.findall('Amy',text) #returns all possible occurances as list in a file or string according to pattern specified ['Amy', 'Amy', 'Amy']
if re.search('ful.$',text): #checks if ends with ful.
    print('ok')
else:
    print('not ok')
if re.search('^Amy',text): #checks if starts with Amy
    print('ok')
else:
    print('not ok')
    
# About patterns
## Character classes
grades = 'ACAAAABCBCBAA'
re.findall('B',grades) # ['B', 'B', 'B']
re.findall('[AB]',grades) # set operator in use to find the occuraces of A and B's perticularly ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A']

re.findall('AB',grades) # to find all occurannes of AB exactly ['AB']
re.findall('AC',grades) # to find all occurances of AC exactly ['AC']
#similarly
re.findall('AB|AC',grades) # ['AC', 'AB']
#more smart similarly
re.findall('[A][B-C]',grades) #means can be AB or AC ['AC', 'AB']
re.findall('^[^C]',grades) #means should start with A or B
#like
print(re.findall('^A|^B',grades))

re.findall('[^B]B',grades) # AB,CB
#like
re.findall('AB|CB',grades)
#like
re.findall('AB',grades) + re.findall('CB',grades)


