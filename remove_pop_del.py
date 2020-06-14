cat = ['a','b','c','d','e']
while cat:
     print(cat.pop())
cat = ['a','b','c','d','e']
print("removing",end= " ")
print(cat.remove('a'))
print(cat)
print(cat.pop(2))
print(cat)
del cat[2] 
print(cat)
