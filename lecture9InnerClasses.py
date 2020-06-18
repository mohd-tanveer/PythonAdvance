#lecture9
#Accessing a class from another class 
#inner classes 

class Employee:
	def __init__(self,eno,ename,esal):
		self.eno=eno
		self.ename=ename
		self.esal=esal
	
	def display(self):
		print('employee number:',self.eno)
		print('employee name:',self.ename)
		print('employee salary:',self.esal)

class Test:
	def modify(emp):
		emp.esal=emp.esal+1000
		emp.display()##calling the display of employee
e=Employee(87245,'ttaama',7000)
Test.modfiy(e)#it is called using class method so above method will be consider as static method(since no decorator is used)
#the output will be 8000
#Accessing one class from another class is possible -- we can also use direclty class name


''' Inner class
	1.the class which is declared inside another class
	2.without existing one type of object if there is no chance of existing another type of object then we should go for inner classes 
	ex .	car 	engine 
		
	class car:---------- outer class
		..........
		class Engine:--------inner class
			.....
	##without exiting of car there is no engine

	eg:

	university(outer) 	departments(inner) #without exisitng university there is no departments

	class Unviersity:
		class Departments:
	
	eg:
		human body 	Head(without existing human there is no head )

	class Human:
		...............
		class body:
			.....................

	without existing of outer class object there is no chance of existing inner class object. Inner class object is always associated with outer calss object.
---Any number of inner classes can be define 
--inner class can be called without outer class object 

eg
	class Human:
		def __init__(self):
			self.head=self.Head()
			slef.brain=self.Head().Brain()
		class Head:
			def talk():
		
			class Brain():
				def think():
'''

class Outer:
	def __init__(self):
		print('outer class object creation')
	def m2(self):
		print('outer class method')
	class Inner:
		def __init_(self):
			print('inner class')
		def m1(self):
			print('Inner class method')

#create outer object
o=Outer()
o.m2()
#create inner class object using outer object
i=o.Inner()
#alter nate 	i=Outer().Inner()
i.m1()
#alternate	 Outer().Inner().m1()


class Person:
	def __init__(self,name,dd,mm,yyy):
		self.name=name
		self.dob=self.DOB(dd,mm,yy)
	def display(self):
		print('Name:',self.name)
		self.dob.display()
	
	class DOB:
		def __init__(self):
			self.dd=dd
			self.mm=mm
			self.yyyy=yyyy
		def display(self):
			print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))

p = Person('sunny',24,5,2101)
p.display()


class Human:
	def __init__(self):
		self.name='jamana'
		self.head=self.Head()
	
	def display(self):
		print('Name',self.name)
		self.head.talk()
		self.head.brain.think()
	class Head:
		def __init__(self):
			self.brain=self.Brain()
		def talk(self):
			print('think')
		def Brain:
			def think(self):
				print('thinking...')
h = Human()
h.dispay()