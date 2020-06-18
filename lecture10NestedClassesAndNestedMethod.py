#Lecture10
#NestedClassesANDnestedMethod
'''
def m1():
	def m2():
		xxxxxxxxxxx
		xxxxxxxxxxx///10000 lines of code repeatedly required in same method
		xxxxxxxxxxx///Code Reusability
'''

class Test:
	def m1(self):
		def sum(a,b):
			print('First Argument:',a)
			print('Second Argument:',b)
			print('the sum is :',a+b)
			print('the Product :',a*b)
			print('*'*20)
	sum(10,20)
	sum(100,200)
	sum(1000,2000)

t=Test()
t.m1()
########################################################
################Garbage Collection######################
########################################################

'''
del t1
t1=none		both are not same 

t1 will be deleted and it will not be deleted in first case
t1 is not deleted just reference is not there so it can be used

garbage collector is run in background and it will free the memory by destroying useless objects

Based on your requirement we can enable and disable GC

##############################
###########Destrutor##########

__del__()

''' 
