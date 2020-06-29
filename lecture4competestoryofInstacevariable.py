#lecture4
#compete story of instance variable

#1. Instace Variable
#============================
''' if the value of a variable is varied from object to object such type of varibles for every object a seprate copy will be created '''

###############################
####   Where we have to decalre instace varible ########
#1.	Inside a Constructor by using self(within class)
#2.	Inside a Instance method by using self(within class)
#3.	from Outseide of the class by using object refrence

###############################################

##############  How To Access instance variables:#######################
'''---within the class by using self 
   ---from outside of the class by using object refrence '''

####################################
'''		How to Delete the instace variable :
------------------------------------------------------
inside the class:		del self.variablename
outside of the class:	del objectrefrence.variablename	'''	

class Student:
	def __init__(self,name,rno):
		self.name = name   #self.name =is a instace varible
		self.rno=rno		#1.	Inside a Constructor by using self
		self.x=10
		self.y=20
	def info(self):
		self.marks=60 #2.	Inside a Instance method by using self(instace variable because it is a decalared using self)
		x=10 ##local variable
		print("hello my name is :",self.name) ##Accessing instance varible using self(within the class)
		print("my roll no is :",self.rno)

	def delete(self):
		del self.x,self.y

	def delete1(self):
		del self##only  self will be delete in case of it is called 

s1=Student('tanv',122)
print(s1.__dict__)###tells how many instace variables are there(2 instace variables)
s1.info()
s1.age=24	#if the varible already exist it will be overwritten otherwise new varaible will be added #this is the 3rd type varible
s1.a=5
s1.c=2
print(s1.__dict__)## three instance variable 
s2=Student('pavan',102)

s2.wife='renu'
print(s2.__dict__)

print(s1.name,s1.rno) ##Accessing outised of the class (usign obect reference varaible)
print(s2.name,s2.rno)
s1.delete()
print(s1.__dict__)## After deleting the instance variable inside the class

del s1.a,s1.c ##deleting outside of the object
print(s1.__dict__)

