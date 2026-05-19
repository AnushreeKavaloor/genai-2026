from abc import ABC, abstractmethod

class Employee(ABC):
	company_name = "TechCorp"
	def __init__(self, name, emp_id, base_salary):
		self.name = name
		self.emp_id = emp_id
		self.base_salary = base_salary
	
	@abstractmethod
	
	def calculate_salary(self):
		pass
	
	def display_info(self):
		print(f"Name: {self.name}, ID: {self.emp_id}, Company: {self.company_name}, Salary: {self.calculate_salary()}")

class Developer(Employee):
	def __init__(self, name, emp_id, base_salary, bonus):
		self.bonus = bonus
		super().__init__(name, emp_id, base_salary)
		
	def calculate_salary(self):
		return self.base_salary+self.bonus

class Manager(Employee):
		def __init__(self, name, emp_id, base_salary, team_size):
			self.team_size = team_size
			super().__init__(name, emp_id, base_salary)
			
		def calculate_salary(self):
			return self.base_salary+self.team_size*100

d = Developer("Siri", 3849, 200000, 50)
m = Manager("Anu", 4678, 300000, 10)
for i in [d, m]:
		i.display_info()
		
