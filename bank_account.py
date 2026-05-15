class BankAccount:
	def __init__(self, acc_holder, balance=0):
		self.__acc_holder = acc_holder
		self.__balance = balance
	def deposit(self, amount):
		if amount>0:
			self.__balance+=amount
		else:
			print("Only positive amount is taken")
	def withdraw(self, amount):
		if amount>0 and amount<=self.__balance:
		    self.__balance-=amount
		else:
			print("Insufficient balance")
	def get_balance(self):
		return self.__balance
	def get_holder(self):
		return self.__acc_holder

my_acc = BankAccount("Mr.Nikil Verma", 100000)
my_acc.deposit(10000)
my_acc.withdraw(50000)
print(my_acc.get_balance())
print(my_acc.get_holder())
