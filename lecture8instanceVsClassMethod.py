#lecture8
##instance method vs class methods
''' Inside method boyd we are acccessing only class level data
what is the need of declaring as instance method

instance method is costly, because to access it require the object of a class where as class method can directly call by class name

--------------------------------------------------
Instance method					vs		class method:

insdie method body if we are using atleast one 		inside method body if we are using only static variables the it is 
instance variable then compulsory we should			highly recomended to decalre that method as class method
decalre that method as instance mthod.

to decalare instance method we are not required to	compulsory we should use @classmethod decorator
used decorator	

the first argumnet to the instance method		the first argument to the class method is cls, which is reference
should be self which is refrence to current object	variable currnet class object and by using that we can access
and by using that we can access static variables	static variables


we can access both variabels 				only static varaibles can be accessed

we can call instance method by using object refrence	we can call classmethod by both ways object refrence and class name
							recomended is to use class name

def instancemethod(self):
	print(self.name)
	print(self.marks)
	print(self.rollno)

@classmethod
def classmethod(cls):
	print(cls.collegename)
	print(cls.bankaname)
'''
