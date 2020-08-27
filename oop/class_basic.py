class Animal:
	name = ''

	def __init__(self,n):
		self.name = n
		print("Animal Named:",n,"is Created")
	
	def play(self):
		print("Your",self.name,"is playing")

	def __del__(self):
		print("Your",self.name,"is destroyed")

animal_object_one = Animal('Life')
animal_object_one.play()
animal_object_one = Animal('Kutu')
print("New animal that you have is",animal_object_one.name)
me = Animal('Dilshad')
