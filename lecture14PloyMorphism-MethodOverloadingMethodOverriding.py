#lecture 14
#method Overloading and OverRiding
#since we do not explicitly define the type of argument method overloading does not require
#instead we can use same method for different differnet type of argument 
#Example
class Test:
	def m1(self,i):
		print(i)

t=Test()
t.m1(10) #output 10
t.m2('durga')#output Durga hence no wory of type of argument because same method can be used but what about different number of argument sometime i want pass 1,2,3

'''	 for that python provides
		 Default arguments
		 variable length argument 

#Example for Default arguments 
class Test:
	def sum(self,a=None,b=None,c=None):
		if (a!=None and b!=None and c!=None):
			print('the sum of 3 number :',a+b+c)
		elif a!=None and b!=None:
			print('the sum of 2 numbers:',a+b)
		else:
			print('please provid 2 or 3 arguments')
t = test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)#else part will be executed 
			

#example of variable length argument

class Test:
	def sum(self,*a):
		total=0	#total ='' for concatenation or to restrict we can check type
		for x in a:
			total = tatal + x
		print('the sum :',total)

t= Test()
t.sum(10,20,30)
t.sum(10,20,30,40,50,60)
t.sum()#output is zero
t.sum(10)


'''	......Cosntructor OverLoading.............
	......Method Overriding :................
	Inheritance:
	---------------------
	class p:
		10 methods
	class C extends p:	#java syntax
		5 more methods

1.	Code Reusability
2.	Existing functionality we can extend
	the syntax

	class p:
		10 methods
	class C(p1,p2,p3):pass(if no method is define)
		5 more methods

'''
class P:
	def property(self):
		print('cash+land+gold+power)
	def marry(self):
		print('laxmi')
class C(p):#pass
	#child is not happy with the marry method so he can redine known as method overriding 
	def marry(self):
		super().marry()##for parrent as well as your own super is used to call immediate parrent method
		print('Katarina..')
c=C()
c.property()
c.mary()

##in java multiple inheritance is not alowed but in python all types of inheritance is possible
	
		