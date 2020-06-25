#lecture 16
''' super();
	from child class to call parent class memebers
	purpose:Code Reusability
#super key word can be used to invoke parent class constructor.
#similarly be call parent calss method
'''
class Person:
	def __init__(self,name,age):
		self.name=name
		slef.age=age
		#simialry 100 propersties can be defined
	def display(self):
		print('name:',self.name)
		print('age:' ,self.age)

class Student(Person):
	def __init__(self,name,age,rollno,marks):
		#self.name=name
		#self.age=age
		#100 propersties needs to take
		##Instead of define each property again we should use super() keyword to define those value
		super().__init__(name,age)
		self.rollno=rollno
		self.marks=marks
	def display(self):
		super().display()
		print('roll no:',self.rollno)
		print('marks:',self.marks)
class Teacher(Person):
	def__init__(self,name,age,salary,subject):
		#self.name=name
		#self.age=age
		#100 Properties needs to defined here as well
		##Instead of define each property again we should use super() keyword to define those value
		super().__init__(name,age)
		self.salary=salary
		self.subject=subject

	def display(self):
		super().display()
		print('salary:',self.salary)
		print('Subject:',self.subject)

s=Student('Ravi',23,101,90)
t=Teacher('youtube',62,1000,'Pyhton')

##Instead of define each property again we should use super() keyword to call

'''	A
	|
	B
	|
	C
	|
	D
	|
	E-----> supper() calls immediate parent if the immediate parent doesn't have then C and then B and then A like MRO algorithm

'''

class A:
	def m1(self):
		print('A class method')
class B(A):
	def m2(self):
		print('B class Method')

class C(B):
	def m1(self):
		print('C class method')
class D(C):
	def m2(self):
		print('D class Method')
class E(D):
	def m1(self):
		super().m1()
#How to call a  particular parent class method using super()
#2 ways 
	#1st method call using class name and method---->parentClassName.MethodName(self)
	B.m1(self)
	#2nd Method call using super-----------> super(D,self).m1()
	super(D,self).m1()# Here the key point is who will get the chance the?---Mehthod C class , super of D class. 
e=E()
e.m1()

''' Loop Holes of super()
	1.from Child class by using super() we cannot call parent class instance variables we should use self only.
	2. from child class by using super() we can call parent class static variables 
'''
class P:
	a=10
	def __init__(self):
		print('Parent constructor')
		self.b=20
	def m1(self):
		print('parent instance method')
	@classmethod
	def m2(cls):
		print('Parent class method')
	@staticmethod
	def m3():
		print('parent static method')
class C(P):
	def __init__(self):
		#print(super().a)
		#print(super().b) #this will throw an error , instead we should use self only
		super().__init__()
		super().m1()
		super().m2()
		super().m3()
	def method(self):
		super().__init__()
		super().m1()
		super().m2()
		super().m3()
#both will work because there is always default constructor
c=C()
c.m1()