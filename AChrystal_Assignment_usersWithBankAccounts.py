
class BankAccount:
	def __init__(self, int_rate=0, balance=0):
		self.int_rate = int_rate 
		self.balance = balance 
		
	def deposit(self, amount):
		self.balance += amount 
		return self

	def withdraw(self, amount):
		# check the balance and see if it's greater than the amount 
		if self.balance >= amount:
			self.balance -= amount 
		else:
			self.balance -= 5 
			print("Insufficient Funds: Charging a $5 fee")
		return self

	def display_account_info(self):
		print(f"Balance: ${self.balance}")
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance + self.balance * self.int_rate
		return self

# Update your previous User class to have an association with the BankAccount class. You should not have to change anything in the BankAccount class. The method signatures of the User class (the first line of the method with the def keyword) should also remain the same.  
# **SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

class User:		
	# def __init__(self, name, email): 
	# 	self.name = name
	# 	self.email = email
	# 	# self.account = BankAccount(int_rate=0.02, balance=0)  #If user just has one account, use this line
	# 	#to allow user to have two accounts and specify between:
	# 	self.checking_account = BankAccount(int_rate=0, balance=0)
	# 	self.savings_account = BankAccount(int_rate=0.03, balance = 0)
	def __init__(self, name, email): 
		self.name = name
		self.email = email
	# self.account = BankAccount(int_rate=0.02, balance=0)  
	# #If user just has one account, use this line
	#to allow user to have two accounts and specify between:
		self.accounts = {
			"checking": BankAccount(0,0),
			"savings": BankAccount(.03, 0)
		}

	def account_deposit(self, amount, account):	# takes an argument that is the amount of the deposit, and specifies the account to deposit to
		self.accounts[account].deposit(amount)	# the specific user's specific account increases by the amount of the value received
		return self

	def account_withdrawal(self, amount, account):	# takes an argument that is the amount of the deposit
		self.accounts[account].deposit(amount) # calls the deposit function in BankAccount class to increase the specific user's account by the indicated amount
		return self

	def display_user_balances(self):
		for key, value in self.accounts.items():
			print(f"{self.name}'s {key} balance: {value.balance} ")
		return self
		
	def transfer_money(self, amount, account, other_user, other_user_account): 
		self.accounts[account].withdraw(amount)
		other_user.accounts[other_user_account].deposit(amount)
		return self	

abbey = User('Abbey Chrystal', 'abbey@codingdojo.com')
guido = User('Guido Cheetoh', 'guido@codingdojo.com')

abbey.account_deposit(1000, "checking").account_deposit(1000, "savings")
abbey.display_user_balances()
guido.account_deposit(500, "checking").account_deposit(500, "savings")
guido.display_user_balances()

abbey.transfer_money(500,'savings', guido, 'checking').display_user_balances()
guido.display_user_balances()


