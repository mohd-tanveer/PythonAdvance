#lecture15
#types of python Inheritance 
'''	IS-A vs Has-A Releationship in python
-------------------------------------------------------------------------------

Is-A relationsip
Maruti IS-A car

Composition vs Aggregatiion---(both are has-a Releationship)

example to understand
Husband vs wife:
-----------
without You i cannot be ==> strong association
	**Composition** 

without you I can be ===> Weak association 
	**Aggregation**

Example of Composition 
	University vs Departments==>>strongly Associated
	Without existing university there is no chance of existing departments 
	**University Has-A Department but strong association

Example of Aggregation
	Departments vs Professor ========> weakly associated
		here say university is shut now the department will vanish but professor can join different department or different university vice versa.
			so professor is not strongly dependent on Professor
'''


class Student:
	collegeName='Youtube' #the college name does not depend on an object student 
	def __init__(self,name):
		self.name=name#without existing an object(student) there is no name so it is strong releation and composition.
print(Student.collegeName)

#Hence relation between class and instance varaible is Composition 
#and relation between class and static variable is Aggregation


'''
	type of Inheritance 
-----------------------------
single Inheritance 
multi level Inheritance 
hierarchical Inheritance 
multiple Inheritance 
hybrid Inheritance 
cyclic Inheritance 
******Python support all the types of inheritance except Cyclic Inheritance***************(no language support it)
advantage:Reusability of the code


1)	Single Inheritance:
-------------------------------------------------------------
Single parent------single Child (single inehritance)
'''
class P:
	def pm1(self):
		print('Parent Method')
class C(P):
	def cm2(self):
		print('child Method')
c=C()
c.pm1()
c.cm2()


'''
2)	Multi-level:
----------------------------------
A
|	all the property of A can be accessed by bcd,
B	all the property of A,B can be accessed by cd
|
C	the property of A,B,C can be accessed D
|
D
'''
class P:
	def pm1(self):
		print('Parent Method')
class C(P):
	def cm2(self):
		print('child Method')
class CC(C):#child of C (or at level 2)
	def ccm3(self):
		print('sub child method')
c=CC()
c.pm1()
c.cm2()

'''
3.	Hierarchical Inheritance
----------------------------------
one parent by multiple childs at same leve 
		p----------parent 
	      /	|  \
	    /	|   \
	  /	|    \
	c1	c2    c3---------Child
'''

class P:
	def m1(self):
		print('Parent Method')
class C1(P):
	def cm2(self):
		print('child1 Method')
class C2(P):#child of P (at same level(hierarchical))
	def cm3(self):
		print('child2 method')
c=C1()
c.m1()
c.cm2()
print()
c1=C2()
c1.m1()
c1.cm3()
	
'''	
4.	Multiple Inheritance 
	p1-m1	p2-m1	p3-m1
	\	|	/
	  \	|      /
	   \	|     /
	     \	|   /
		C
	at child level if i call the m1 then which method should call?
##this problem is known as Ambiguity Problem or Diamond Access Problem(because of this java does not provide)
but python provide the support
'''
class P1:
	def m1(self):
		print('p1 method')
class P2:
	def m1(self):
		print('p2 method')
class C(P1,P2):#pass#based on this order C(P2,P1)
	def m1(self):
		print('child method') #now child will be consider first

c=C()
c.m1()#which will come?
#in python it works in order of class by which it is defined here p1 will get higher proprty if if no then p2
#example of Primary Contact number and secondary contact number 
#Example of Permanent Address and current address
#example of Nominee first nominee will be consider first

#so here if m1 is available in p1 then it will call other wise p2
#Child and then Parent 1 and then parent2 

'''
5.	Hybrid Inheritance (combination of Multilevel and Multiple inheritance)
	A	B	C
	\	/\	|
	 \     /   \	|
	  \   /	     \	|
	    X	      	Y	D
	    \		/	|
	      \	       /	/
		 \    /	      /
		    Z  /  /  /
		    |
		    |
		    |
		    M

6. Cyclic Inheritance ....
			class A requires all property of class A 
	class A(A): (what is the need, example of state A in DFA loop to itself)
'''
