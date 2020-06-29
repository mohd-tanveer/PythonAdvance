#lectrue1
'''###Oops class objects|refrence variable in python.
#example of Tvs
	design is a class
	each pyhysical tv is ===>object
#example of Ganpati idol
	market==>Mold/dye
	plastic company==>5 cr
	5 different sizes
	3 lakkhs= mold/dye

		based on same mold/dye we can create n number of buckets with the same size
		mold/dye==class
		physical bucket==object


Class ===Blueprint/template/mold/dye/plan for objects
Object===is physical existence of a class
	physcial instance of a class

#Refrence Variable
	sony high end xyz model design
			/\
		/		\
	/				\
object 1(tv1)		object 2(tv2)
	|
	remote(it is refrence variable tv can be accessed with remote )


class object ==>one to many
object refrence vaiable ===> one to one many(multiple vairbale pointing to same object/pointer)==one to one| one to many(example of two remote for a single tv)	'''

class student:
	'''document string'''
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
	def talk(self):
		print("hello my name is :",self.name)
		print("hello my roll no is :",self.rollno)

#object
s=student(100,'sunny')
print(s.name)
print(s.rollno)
s.talk()
s1=student(200,'bunny')
s1.talk()

