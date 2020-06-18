##Lecture7

##instance method,Getter,setter method
'''
instance method
def m1(self):
	self.x
	WE are using instance variable
@classmethod
def m1(cls)
	cls.x
	Test.x
@staticmethod
def add(x,y):
	print(x,y)
'''
##syntanx
#def setVariableName(self,variableName):
#	self.variableName=variableName
# set and get method is used for individaul variables



class Student:
	def setName(self,name):
		self.name=name

	def getName(self):
		return self.name


	def setMarks(self,marks):
		self.marks=marks

	def getMarks(self):
		##validation stuff
		return self.marks

n=int(input('enter number of studnet:'))
for i in rnage(n):
	name=input('enter name')
	marks=int(input('enter marks'))
	s= Student()
	s.setName(name)
	s.setMarks(marks)
##print(s.name)//direct access no validataion
##whhere as set and get used to hide the data behind methods(hiding data behind methods===> Encapsulation)