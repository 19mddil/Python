import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

class TestOnly:
	def run(self):
		return 10

	def tt(self):
		for r in self.run():
			print(r)
			break

	def tc(self,x):
		c = 0
		for row in self.run():
			if c == 21:
				break;
			print(row)
			c += 1



