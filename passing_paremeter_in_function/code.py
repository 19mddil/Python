# variable number of non keyword arguments passed 

# function definition 
#We do not know how many arguments will be given
def calculateTotalSum(*arguments): #arguments passed behaves like a tuple
	totalSum = 0
	for number in arguments: 
		totalSum += number 
	print(totalSum) 
def dasterisk(arg,**param):
	print(arg)
	print(type(param))
	for (k,v) in param.items():
		print("key :",k," Value:",v)

# function call 
calculateTotalSum(5, 4, 3, 2, 1)
dasterisk('Dilshad',a=1,b=2,c=3)

