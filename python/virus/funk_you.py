import os
import random
#import time
str = 'abcdefghijklmnopqrstuvwxyz'
while True:
	m = random.randint(0,25)
	n = random.randint(0,25)
	o = random.randint(0,25)
	p = random.randint(0,25)
	command = 'mkdir '+str[m]+str[n]+str[o]+str[p]
	os.system(command)
	#time.sleep(4)



