#lecture12
#Ploymorphism
#duck typing phylosophy of python
#overloading
	#Operator Overloading
	#method overloading
	#Constructor oberloading --all three not supported  if you define method overlaoding python will consider only last method already discussed in previous lecture.
	
#overriding
	#method Overrding
	#Constructor Overriding 
	
#Polymorphism
##############################
'''	
	Poly means many
	morphs mean forms

one name but multiple forms

Example of Polymorphism :
	A person like us:	AT Home : our Behaviour is different talks about class,book,temple,college
			outside home with Friends:Here the behaviour is diefferent brand,cigar,cinema,park
			At School : Different Behvaiour 
			At sports Ground : Different behaviour
			oustide of native place: Exactly different behaviour
one man with multiple forms(poly morph ism)

################	Overloading  ###############################

10+20====>>> 30
'You'+'Tube'==>>Youtube

same operator but multiple bhevaiour at first place it is doing addition and at second place it is doing concatenation
10*3=30
'durga'*3===>durgadurgadurga
here * is an example of method overloading same operator but different behaviour(polymorphism)

	deposit(cash)
	deposit(cheque)
	depsoit(dd)

	#same name but argument type is different
	abs(int i)
	abs(long i)
	abs(float i)

#########################	 Operator Overloading	######################
*in java there is no Operator overlaoding but in python it does support we have already seen an example of plus and *
'''

class Book:
	def __init__(self,pages):
		self.pages=pages
b1=Book(100)
b2=Book(200)
print(b1+b2)##it will send an error as unsuported operator but we can extend

#to use this we need to define magic method in the Book class 
#so Operator Overloading is defined internally by Using magic Methods
#	+==============>>	__add__(self,other)

class Book:
	def __init__(self,pages):
		self.pages=pages
	def __add__(self,other):##	'self' will be considered for b1 and 'other' will be consider b2
		return self.pages + other.pages
	def __sub__(self,other):##	'self' will be considered for b1 and 'other' will be consider b2
		return self.pages + other.pages
	def __mul__(self,other):##	'self' will be considered for b1 and 'other' will be consider b2
		return self.pages + other.pages
	def __div__(self,other):##	'self' will be considered for b1 and 'other' will be consider b2
		return self.pages + other.pages

	
b1=Book(100)
b2=Book(200)
print(b1+b2)
#output 300 #Python will call internally
print(b1*b2)
print(b1-b2)
print(b1/b2)


'''	MAGIC METHODS
+==>	__add__()
-==>	__sub__()
*==>	__mul__()
/==>	__div__()
%==>	__mod__()
//==>	__floordiv__()
**==>	__pow__()


+=	==>	__iadd__()
-=	==>	__isub__()
*=	==>	__imul__()
/=	==>	__idiv__()
%=	==>	__imod__()
//=	==>	__ifloordiv__()
**=	==>	__ipow__()

>	==>	__gt__()
>=	==>	__ge__()
<	==>	__lt__()
<=	==>	__le__()
==	=>	__eq__()
!=	==>	__ne__()


