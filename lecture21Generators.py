#Genrator functions
'''
	to generate a sequence of values
		##yield Keyword ##
'''

def mygenrator():
	yield 'A'
	yield 'B'
	yield 'C'

g=mygenrator()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
''' I can also defined those values in list=[a,b,c] then what is the difference between.
 	 example 1.	storing 60 rice bag for 60 months -example of list
 	 		 2.	ordering 1 rice bag for everymonth -example of generator
 	 	in first case there will be wastage of memory. while in second one we are not wasting memory
'''
#l=[x*x for x in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)]
#above list can give memory error , hence recomended to use generator
'''
g=(x*x for x in range(100000000000000000))
while True:
	print(next(g))#yield keyword will be taken care by python
'''
import time
def countdown(num):
	print('count down start....')
	while (num>0):
		yield num
		num=num-1
values=countdown(10)
for x in values:
	print(x)
#	time.sleep(1)

def firstn(num):
	n=1
	while n<=num:
		yield n
		n=n+1
for x in firstn(10):
	print(x)

#to genrate number
# 0,1,1,2,3,5,8,13,21....
def fibonacci():
	print('fibonacci of n mumbers')
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b

for n in fibonacci():
	if(n>1000):break
	print(n)

import random
names = ['sunny','bunny','chinny','vinny']
subjects = ['python','java','Blockchain']

def people_list(num):
	#results=[]
	for i in range(num):
		person={
		'id':i,
		'name':random.choice(names),
		'subject':random.choice(subjects)
		}
		yield person #instead of list lets use generator 
		#results.append(person)
	#return(results)


t1 = time.clock()
people=people_list(100)
t2=time.clock()
print('time taken:',t2-t1)
for n in people:
	print(n)
#output genrated will be same in both the case but time taken in genrator is very less