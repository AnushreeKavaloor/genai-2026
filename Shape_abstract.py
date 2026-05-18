from abc import ABC, abstractmethod
import math

class Shape(ABC):
	@abstractmethod
	def calc_area(self):
		pass
	def describe(self):
		print("This is a Shape.")

class Triangle(Shape):
	def __init__(self, side):
		self.side = side
	def calc_area(self):
		print(f"Area of Triangle is {(math.sqrt(3)/4)*self.side**2:.2f}")

class Rectangle(Shape):
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def calc_area(self):
		print(f"Area of Rectangle is {self.length*self.breadth}")

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	def calc_area(self):
		print(f"Area of Circle is {(22/7)*self.radius**2:.2f}")

T = Triangle(6)
R = Rectangle(10, 20)
C = Circle(5)
T.calc_area()
T.describe()
R.calc_area()
R.describe()
C.calc_area()
C.describe()
