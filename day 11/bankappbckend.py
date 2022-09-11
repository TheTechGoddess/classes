from models import Session, User
import secrets


session = Session()



class ItechBank():

	def create(self,name,balance):
		self.name = name
		self.balance = balance
		self.account_id = secrets.token_hex(5)
		user = User(fullname = self.name, balance = self.balance, account_id = self.account_id)
		session.add(user)
		session.commit()
		print(f'{self.name} with {self.account_id} and N{self.balance} has been created successfully')

	def check_balance(self):
		self.balance-=10
		self.balance = amt
		print(f'Your balance is N{self.balance}')	

	def deposit(self,amount,depositor):
		self.balance+=amount
		print(f'{depositor} paid in {amount} to your account. Your new balance is {self.balance}')

	def withdraw(self,amount):
		if self.balance >= amount:
			self.balance-=amount
			print(f'Your account has been deducted by {amount}, and your new balance is {self.balance}')
			return True
		else:
			print('insufficient funds')	
			return False

	def transfer(self,amount,user):
		if self.withdraw(amount):
			user.deposit(amount, self.name)


'''user1 = ItechBank('Ikem Nodebe', 2000)
user2 = ItechBank('Lissa', 3000)	

user1.transfer(500,user1)'''

#user1.check_balance()		

#user2.deposit(8000, 'Presh')

#user2.withdraw(3000)

