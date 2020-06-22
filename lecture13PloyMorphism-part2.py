##polymorphism-2
#Operator overloading 2
#let's try to print the object

class Book:
	def __init__(self,pages):
		self.pages=pages
b1=Book(100)

''' output :	main<>.object at x0246036

class Book:
	def __init__(self,pages):
		self.pages=pages
	
	def __str__(self):
		return('the number of pages :'+str(self.pages)) ##both should of of string type for concatenation
		#it is used just as print purpose of type string
	
	#def __add__(self,other):
	#	self.pages+other.pages

	def __add__(self,other):
		total=self.pages+other.pages
		b=Book(total)
		return b 
	#Similarly we can use __mul__ and other operator 
	def __mul__(self,other):
		total=self.pages+other.pages
		b=Book(total)
		return b 
	
b1=Book(100)
print(b1)##it will call __str__
b2=Book(200)
print(b1+b2)#it will call __add__
b3=Book(300)
print(b1+b2+b3)# output will be unsupported(b1+b2) is int type and B3 is Book Type , to overcome this let's modify __add__
#now the output will be 300 with return type as Book ---600
b4=Book(700)
print(b1+b2+b3+b4)## now we can add as many as possible

'''	Whenever we are calling + operator then __add__() method will be called 
	whenever er are printing object reference then __str__() method will be called 
'''
print(b1+b2*b3+b4) #the output will be: the number of pages:60700

##example 2

class Student:
	def __init__(self,name,marks):
		self.name=name
		slef.marks=name
	
	def __lt__(self,other):
		self.marks<other.marks
s1= Student('durga',100)
s2= Student('Sabi',200)
print(s1<s2) #we want to compare the marks of student.

##example 3

class Employee:
	def __init__(self,name,salary):
		self.name=salary
		slef.salary=salary
	
	def __mul__(self,other):
		return self.salary*other.days

class TimeSheet:
	def __init__(self,name,days):
		self.name=name
		self.days=days
	def __mul__(self,other):
		self.days*other.salary
e=Employee('tanv',800)
t=TimeSheet('tanv',25)
print('this months salary is',e*t)
print('this months salary :'t*e) #to work this we need to define the __mul__ in Timehseet 

############	Method Overloading	#############
####################################################
#	same name of method but different argument types 
# but in python we never define the argument type hence python does not support Method Overloading
# However if we write method overloading  last method will be called everytime
#example
class Test:
	def m1(self):
		print('no-arg method):
	def m1(self,x):
		print('no-arg method):

t=test()#it will not work because as soon as we decalre the second method with the same name first method gone
t=test(11)#it will work 
#let's discuss alternate method in next class
	