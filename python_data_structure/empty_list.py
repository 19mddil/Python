#it is a empty list
print([])

fruit = 'Banana'
try:
    fruit[0] = 'b'
except:
    print('Strings are not mutable aka immutable')
#But lists are mutable
lotto = [2,3,4,5,'j']
lotto[-1] = 10
print(lotto) #as lists are mutable.
