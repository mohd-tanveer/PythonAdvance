#MultiThreading
#part1,part2 and part3
'''
-------------------
Multi tasking:	1. A student is listining the class
				2. Writing Running Notes
				3. Checking important Notification
				4. Sleeping
				5. checking Enviornment
		executing several task simultaneously

	1.	Process Based Multi Tasking
	-----------------------------------
				each task is a seperate indepedent process
				example- typing a python program in the editor and listening audio songs from the same system and 
					downloading new songs from the internet
			also each of them is independent with each other

		Os level

	2.	Thread Based Multi Tasking
		----------------------------
		within one process execute the multiple thread
		in a single program execute multiple thread to improve the execution

		1.	An Independent part of program 
		2.	A flow of execution is considered as thread
		3.  It is a python Object

		for every thread independent job is available 

		example: gmail can be accessed by multiple person-server implementation 
		---Python Provides In-Built Functionality threading

		#####	3 Ways To create thread
		1.	Creating a Thread without using any class
		2.	creating a thread by extending thread class
		3.	creating thread without extending thread class
		'''
'''#type1 
#import threading   #we must need to use module name 
#print('Current executing thread: ', threading.current_thread().getName())

from threading import * # directly we can use method name
def Display():
	for i in range(10):
		print('Child thread')

t=Thread(target=Display) #creation of thread object to execute display
t.start()
for i in range(10):
	print('Main Thread')
#output will mix of main thread and child thread
'''

#type2 creating a thread by extending thread class
'''
from threading import * # directly we can use method name
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print('child thread',current_thread().getName())

t=MyThread()
t.start()
for i in range(10):
	print('Main Thread',current_thread().getName())

#type3 without extending class
from threading import *
class Test:
	def m1(self):
		for i in range(10):
			print('child thread',current_thread().getName())
obj=Test()
t=Thread(target=obj.m1)
t.start()
for i in range(10):
	print('main thread',current_thread().getName())


#example
import time
from threading import *
def doubles(numbers):
	for n in numbers:
		time.sleep(1)
		print('double value',2*n)

def squares(numbers):
	for n in numbers:
		time.sleep(1)
		print('squares value:',n*n)
numbers=[1,2,3,4,5,6,7]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))#args should of tuple
t2=Thread(target=squares,args=(numbers,))
#doubles(numbers)
#squares(numbers)
t1.start()
t2.start()#main thread will not wait 

t1.join()
t2.join()#these lines will restrict the main thread to execute
endtime=time.time()
print('total time taken: ',endtime-begintime)

'''
'''
setting and getting name of a thread
----------------------------------
#to get name
t.getName()
t.name

or 
#to set name
t.name='thread name'
t.setName(name)

from threading import *
print(current_thread().getName())
#current_thread().name='durani'
current_thread().setName('my main thread')
print(current_thread().getName())
#print(current_thread().name)
'''
'''
THread identification Number:
#for every thread there is unique identification number is available 
from threading import *
def test():
	print('child thread')


t= Thread(target=test)
t.start()
print('main thread identification number: ',current_thread().ident)
print('child thread identification number: ',t.ident)
'''
'''
active_count():
---------------
total number of active threads
'''
'''
from threading import *
import time
def display():
	print(current_thread().getName(),'....started')
	time.sleep(3)
	print(current_thread().name,'....ended')#name function both ways
print('the number of active threads', active_count())

t1= Thread(target=display,name='Child thread 1')#if not provided pvm will provide by default
t2= Thread(target=display,name='Child thread 2')
t3= Thread(target=display,name='Child thread 3')
t1.start()
print('the number of active threads', active_count())
t2.start()
t3.start()
print('the number of active threads', active_count())
print(t1.name,'is alive: ',t1.isAlive())
print(t2.name,'is alive: ',t2.isAlive())
print(t3.name,'is alive: ',t3.isAlive())
'''

#time.sleep(10)
#print('the number of active threads', active_count())

'''
enumerate():
-------------------------------------
to enumerate list of active thread 

l=enumerate()
for t in l:
	print('thread name',t.name)
	print('thread identification number:',t.ident)

time.sleep(10)
print('the number of active threads', active_count())
print(t1.name,'is alive: ',t1.isAlive())
print(t2.name,'is alive: ',t2.isAlive())
print(t3.name,'is alive: ',t3.isAlive())
'''
'''
isAlive()
-------------
to check if thread is alive
'''
'''
join() method : if a thread wants to wait for other thread
example marriage preparation

Venue Fixing(t1)	wedding cards printing(t2) 	wedding cards distribute(t3)
					wait for t1 to be completed	wait for t2 to be completed

here an user can ask every thread is waiting for another then what is the point of multi threading 
but under wedding cards printing except venue part everything else can be decided
also wedding cards can be divided under different categories 
from threading import * 
import time
def display():
	for i in range(10):
		print('seetha thread....')
		time.sleep(2)

t = Thread(target=display)
t.start()
t.join(10)#wait for t1 to be completed(wait for this much timer )
#display()
for i in range(10):
	print('main thread')

'''

#Part3
'''
	example of multi-threading 

I need to send email to 20,000 user stored in database and also make sure that email does not do multiple times,
so how may i achieve through multi-threading.
2*10k
l1-------> 10k mail ids
l2-------> 10k mail ids

def send_mail(list):
	send mail to every email in list
t1 = Thread(target=send_mail,args=(l1,))# , is because the value is tuple type in case of there is single value example t=(10) this will be considered as int not tuple hence declare as t=(10,)
t2 = Thread(tagets=send_mail,args=(l2,))
t1.start()
t2.start()


###########	Daemon THreads: #####################
-------------------------------------------------
1. the threads may run in the background such type of thread is known as Daemon threads

example:	We can see only few people in movie screen but there are many people in background
	example background : camera man, director,producer , makeup-artist, staff,singer,lyricist,choreographer etc
	without these people actors and actress can't come on screen

2. the main purpose is: to support for non-daemon threads(main thread)
	example : Garbage collector (it will never come on screen , whenever main thread faces any memory problem garbage collector provides memory via clearing the unused memory )

#######these point available for every programming language 

	to check if the thread is daemon thread or not

	t.isDaemon() or
	t.daemon

#to change the daemon nature
to set non daemon thread to daemon 
t.setDaemon(True)
t.setDaemon(False)

exception : to change the daemon nature the thread should not in  active state (if its already started)
			by default the main thread is non-daemon(only main thread is non - daemon )

			t(parent)--->t3(child)....(daemon nature is inherited from the parent)
from threading import *
mt =current_thread()
print(mt.name)
print(mt.isDaemon())
print(mt.daemon)
#mt.setDaemon(True)# it will throw an error because main thread is active but it is already active so we can not change

# to change Daemon nature of the thread is t.setDaemon(true)
from threading import *
def job():
	print('execute the cild thread')

t= Thread(target=job)#this thread will be started by main thread hence this is non-daemon
print(t.isDaemon())#false
#let's change before the start
t.setDaemon(True)
print(t.isDaemon())
'''

from threading import *
import time
def job1():
	print('execute by t1')
	t2=Thread(target=job2)
	print('t2 is Daemon:',t2.isDaemon())
	t2.start()

def job2():
	print('execute by t2')

t1=Thread(target=job1)
print('t1 is Daemon:',t1.isDaemon())
t1.start()
time.sleep(5)

#when ever last non-daemon thread terminates automatically all daemon threads will be terminated we are not required to terminate explicitly
print('end of main thread')
