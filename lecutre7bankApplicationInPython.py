#pythonContinue
#lecutre6
#AfterStaticVariable
#Bank Application By using Python
#globalVariable:can be accessed within and outside of the class.
#Local varibale has the highest Property over Global variable
#GLoabl Functionality is  functional programming concept.
#global variable can be defined under any method  with Global Keyword ex-global
#we can access global variable directly from the class5+
'''
class Test:
	def m1(self):
		global x
		x=888
		print(x)
	
	def m2(self):
		print(x)

'''

class Customer:
	'''Customer class with bank related Operations'''
	bankName='PiggyBank'
	
	def __init__(self,name,balance=0):
		self.name=name
		self.balance=balance
	
	def deposit(self,amt):
		self.balance=self.balance+amt
		print('After deposit the balance:',self.balance)
	
	def withdraw(self,amt):
		if(amt>self.balance):
			print('Insufficient funds...can not perform this operation')
			sys.exit()
		self.balance=self.balance-amt
		print('after withdraw the balance : ',self.balance)

print('Welcome to the ',Customer.bankNmae)
name=input('enter your name')
c=Customer(name)
while true:
	print('d-deposit\nw-withdraw\ne-exit')
	option = input('choose your option')
	if (option.lower()=='d'):
		amt=float(input('enter your ammout'))
		c.deposit(amt)
	else (option =='w' or option=='W'):
		amt=float(input('Enter amount to withdraw:'))
		c.withdraw(amt)
	
	elif option=='e' or option=='E':
		print('thanks for banking')
		sys.exit()
	else:
		print('choose valid option')
	


