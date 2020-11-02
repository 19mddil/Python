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
