class PaymentMethod:
	def __init__(self, amount):
		self.amount=amount
	def process_payment(self):
		print("Processing payment")

class CreditCard(PaymentMethod):
	def __init__(self, amount, card_number):
		super().__init__(amount)
		self.card_number=card_number
	def process_payment(self):
		print(f"Processing ₹{self.amount} via credit card ending in {self.card_number}")

class PayPal(PaymentMethod):
	def __init__(self, amount, email):
		super().__init__(amount)
		self.email=email
	def process_payment(self):
		print(f"Processing ₹{self.amount} via PayPal account: {self.email}")

class UPI(PaymentMethod):
	def __init__(self, amount, upi_id):
		super().__init__(amount)
		self.upi_id=upi_id
	def process_payment(self):
		print(f"Processing ₹{self.amount} via UPI: {self.upi_id}")

payments = [CreditCard(100, 6789), PayPal(1000, "xyz@gmail.com"), UPI(300, 748492)]
for payment in payments:
	payment.process_payment()
