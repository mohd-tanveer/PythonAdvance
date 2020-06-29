#lecture5Complete story of Static varaiable
''' Instance varaible 								--vs--			Static variable
	for every object a seprate copy maintained					for all objects a single copy maintained at class level

ex.	100students===> system,pen,headset,								for 100 students or n mumber of students only one faculty
	notes(seprate things for every students)							member is required.
'''
##########What are the various places are there to decalre static varibales?########
#1. Within the class directly but from outside of any method
#2.	Inside constructor by using class name
#3.	Inside instance method by using classname
#4. Inside a classmethod by using cls variable or class name #4th and 5th already discussed in first lecture.
#5. Inside a static method by using class name
#6 outside of the class by using class name

###########			How TO access static variable 	####
#----------------------------------------
# we can access static variables either by class name or by object refrence

#1.	within theh class we can access by using class name,cls,self
#2.	outside of the class:
#	object refrence , class name


##BY default every variable is public in python
class Student:
	cname="YouTube" ## decalre static variable  type1

	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
		Student.a=10  ##declare static variable type 2 # using class name
		print("insdie a constructor")
		print(Student.cname)# access using class name type1(accessType1)
		print(self.cname)##access using self type1(accestype1)

	def method1(self):
		Student.b=30 ##declare Static variable type3 #using class name inside instance method.
		print("inside instance method")
		print(Student.cname,self.cname)# type1(accestype1)

	@classmethod #type4
	def m2(cls):
		cls.d=40
		Student.e=50#decalre 
		print("insdie a classmethod") #access type
		print(Student.cname,cls.cname)

	@staticmethod #type5
	def m3():
		Student.f=60
		print("inside a staticmethod") #access type1
		print(Student.cname) #only class name


'''s1=Student('tanveer',101)
s2=Student('mano',102)
print(s1.name,s1.rollno,Student.cname)
print(s2.name,s2.rollno,Student.cname)'''
Student.g=70 ##type 7
print(Student.__dict__)
s1=Student('tanveer',101)
s1.method1()
s1.m2()
s1.m3()
print(Student.__dict__)
print("outside of the class by class name or refrence",Student.cname,s1.cname)##recomended to use class 


###		How to Modify the static variable name:
'''		
	1.	within the class we should use class name,cls variable

	2.	outside of the class : using only class name
'''
'''
	how to delete the static variable:
	---------------------------------
	1.	within the class we should use classname,cls variable
	2.	from outside of the class: only ClassName

'''
class Modify:
	a=10
	g=352
	e=585
	def __init__(self):
		Modify.a=20#modify using class name
		self.a=800000#not a correct way to modify
		del Modify.g
	@classmethod
	def m1(cls):
		cls.a=700000 # modifying the variable using cls 
		Modify.a=40 ##modfiying inside class method using class name or cls variable 
		del cls.e #or del Modify.g

	@staticmethod
	def m2():
		Modify.a=50  ##insdie a staticmethod using only class name


t = Modify()
t.m1()
t.m2()
t.a=60
print(Modify.a)#this will print 20
print(t.a)


