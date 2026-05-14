class Dog:
	def __init__(self, name, breed):
	    self.name=name
	    self.breed=breed
	def bark(self):
		print(f"{self.name} says Woof!")
	def info(self):
		print(f"{self.name} is a {self.breed}")

my_dog = Dog("Rex", "Golden Retriever")
my_dog.bark()
my_dog.info()
		
