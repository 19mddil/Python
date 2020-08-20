# variable number of non keyword arguments passed 

# function definition 
#We do not know how many arguments will be given
def calculateTotalSum(*arguments): 
	totalSum = 0
	for number in arguments: 
		totalSum += number 
	print(totalSum) 

# function call 
calculateTotalSum(5, 4, 3, 2, 1) 

