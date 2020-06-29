#Lecture2
##Story of self variable 
class employee:
	'''doc string (description) this is the documentation string we can access it using classname.__doc__'''
	def __init__(self,x,y,z,w):#constructor or current object
		self.x=x
		self.y=y''' these are the instance variable name'''
		self.z=z
		self.w=w
	def info(self):#method(self points to the current object)
		x=8989#(local variable will get more privillege)
		print("Employee Number:",x)#it awill point to local variable
		print("Employee Number:",self.x)#it will point to current object
		print("employee name",self.y)
		print("Employee sal:",self.z)
		print("employee addr",self.w)

e1=employee(100,'durga',1000,'hyd')
e3=employee(x=100,z=1000,y='turga',w='hyd')

e2=employee(200,'pavan',2000,'chn')
e3.info()#there are 5 variable but we need not to provide pvm will provide that.


print(employee.__doc__)##it will tell the doc string which is decalred under class
#help(employee) tells everything about the class

##self variable
'''self variable always points to the current variable self is similar to thi keyword in java, self is pointing to the same object
so id(address) will be same for both of them to access the object from outside we can create an object to access inside the class 
we use self since it points to the same object
__init__ is default constructor for the class 
'''
##TO refer the curent object we use self it will always point to current object.
##The firs argument to the costructor and instance method should be self.
##python virtual machine is resposisble to provide value for slef argument and we are not required to provide explicitly.
#By using self we can decalre instance variables
#By using slef we can  access instance variable
class Student:
	def __init__(self):
		print(id(self))
s=Student()
print(id(s))

##instead of self varaible you can use any other variable but it is recomended to use self 
##what ever is the first variable python automatically assumes it as self
