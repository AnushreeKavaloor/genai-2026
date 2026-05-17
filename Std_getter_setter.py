class Student:
	def __init__(self, name, marks = 20):
		self.name = name
		self.__marks = marks
		#marks is private: can't change from outside
	def get_marks(self):
		#getter method: safely read the private marks
		return self.__marks 
		
	def set_marks(self,marks):
	   	#only allow valid marks between 0 to 100
	   	if marks>=0 and marks<=100:
	   		self.__marks = marks
	   	else:
	   		print("Invalid marks!") #Reject bad output
#–––Test cases to prove it works–––
s = Student("Anu" )
print(s.get_marks()) #Should print 20
s.set_marks(-70) #Test invalid input 
print(f"After Setting marks to -70: {s.get_marks()}") #Should still print 20
s.set_marks(150) #Test invalid input
print(f"After setting marks to 150: {s.get_marks()}") #Should still print 20
s.set_marks(65) #Test valid input
print(f"After setting marks to 65: {s.get_marks()}") #Should print 65
 
