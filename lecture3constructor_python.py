#lecture3
##Cosntructor
#Special method in pyhon
#the name should be alwyas : __init__() 
#whenever we are creating object constructor will be executed automatically and we are not required to call explicitly
#the main objective: to declare and initialize variables
#for every object constructor will be executed only once
#atleast one argument self
#python will provide default constructor if not decalred

class Test:
	def __init__(self):
		print("constructor execcuted")
		self.x=10#instacne variable (usig self )
		self.y=20
	#Constructor Overlaoding()#when ever we define second one only it will be considered (most recent is used), no concept of overlaoding in python
	def __init__(self,x):
		print("one argument:Overlaoded Cosntructor")

t= Test(1)

##we can decalare as many as constructor we want but python will consider only the lattest one. so technically not allowed, same for overlaoding


class Student:
	college_name="COllEGENAME"		#STATIC VARAIBLE
	def __init__(self,name,rollno):
		print("constructor execcuted")
		self.name=name
		self.rollno=rollno		#instance variable using self
	#Constructor Overlaoding()#when ever we define second one only it will be considered (most recent is used), no concept of overlaoding in python
	def display(self):		#instance methods
		print("method execution")
		print("hello my self is:",self.name)
		print("my roll no is :",self.rollno)

	@classmethod#Decrator it will treated as class level variable
	def getCollegeName(cls): #cls-is used for current class level object #cls variable is used to use class variable
		print("college name:",cls.college_name)

	@staticmethod #we need to use this otherwise it will be trated as instace method
	def findAverage(x,y):
		print("Average:",(x+y)/2)


s= Student('tan',100)
s2= Student('man',200)#Instance variable(decalared at object varible )
s3= Student('sab',300)

s.display()
Student.getCollegeName()
s.findAverage(10,20)


''' method 									|				Constructor

	1.the name can be anything				--				should be __init__()
	2.method will be executed if we callled --				will be executed automatically if we are creating an object
	3.per object method can be
	 callled any number of times 			--				per object only once
	4.Buisness logic						--				to declare and initialize instance variables'''

	#there types of variabes
	#1.instance variables/object level variables-using self
	#2.staitc variables/class level variable
	#3.local variables/method Variable--inside a method,self will not be used

	#three types of methods:
	#1.instance methods
		#inside a method if we are using an instance variable then it is called as instance variable
	#2.class methods--since overloading method is not allowed in python this is used@classmethod
	#3.static methods--directly we can used using the object or class name

