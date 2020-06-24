'''#lecture16
Hybrid Inheritance = Single + multiple + multilevel + Hierarchical
#MRO: MRO ALGORITHM
 	A
B  		C

	D

method resolution order of A:it will search in B then object ===>A,object
method Resolution order of B: it will search in B,A,Object
Method resolution of order of C: it will search in C,A,Object
Method Resolution of order of D:D,B,C,A,O
'''
class P:pass
class C(P):pass
	def m1(self):
		print('child method')

c = C()
c.m1()
#if child does not have method it will call parent if parent doesn't contain then parent so on.
print(c.mro())#it will tell the order of the resolution of the child object c
p = P()
p.m1()
print(p.mro())


'''

method resolution order of A:it will search in B then object ===>A,object
method Resolution order of B: it will search in B,A,Object
Method resolution of order of C: it will search in C,A,Object
Method Resolution of order of D:D,B,C,A,O
'''
class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

''' output 
	[<class '__main__.A'>,<class 'object>]
	[<class '__main__.B'>,<class '__main__.A'>,<class 'object>]
	[<class '__main__.C'>,<class '__main__.A'>,<class 'object>]
	[<class '__main__.D'>,<class '__main__.B'>,<class '__main__.C>,<class '__main__.A'>,,<class 'object>]


example 
			O
	      
A(conn:O)	     B(conn:O)		C(connected o)

     X(conn:AB)		     Y(conntected b,c)
		
		P(Conected to xyc)

mro(O)==object
mro(A)=A,O
mro(B)=B,O
mro(C)=C,O
mro(X)=X,A,B,O
mro(Y)=Y,B,C,O
mro(P)=P,X,Y,C,A,B,O
'''
class A:pass
class B(A):pass
class C(A):pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(P.mro())
#output
#	P,X,A,Y,B,C,O 
#the above output does not match our guessed one so to make sure that it is right there is an alorithm C3 Algorithm
'''			take merge of each immediate parent 
	mro(P)	=P+merge(mro(X),mro(Y),mro(C),XYC)
	      	=P+merge(XABO,YBCO,CO,XYC)
		=P + X +merge(ABO,YBCO,CO,YC)# so X will be removed from everylist because it is not present in tail list of anyother list
		=P + X + A + merge(BO,YBCO,CO,YC)#B is present in the tail part of second list so Choose Y second list
		=P + X + A + Y + merge(BO,BCO,CO,C)#Y will be removed from everylist because it is not present in tail list of anyother list
		=P + X + A + Y + B + merge(O,CO,C)#B will be removed from everylist because it is not present in tail list of anyother list
		=P + X + A + Y + B + C +merge(O,O) #O is present in the tail part of second listso choose C from second list
		=P + X + A + Y + B + C +O
		=pxaybco
		
ABCDEF
HEAD ELMENT A
tail elemnt BCDEF
*if head element of first list not present in the tail part of any other list then consider that element
in the result and remove that element from all the lists.



