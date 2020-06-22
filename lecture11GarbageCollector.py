#Lecture11
#####################################################################################
###############################	Garbage Collection	#############################
#####################################################################################

'''
garbage collector is used to destroy the unused memory

gc module

gc.isenabled()  #to check if garabge collector is enabled
gc.disable() # TO desable the garbage collector
gc.enable()	# to enable the garbage collector

'''

import gc
import time
print(gc.enabled)# to enable garbage collector
print(gc.disbaled) #to disable the garbage collector
__del__(self) #destructor
	# it is used to close db connection , To close network Connection
	# Garbage calls the destructor automatically for cleanup activity
	# in java we have finalized method where as here we have __del__(self) destructor

##Just before destrying an object GC always calls destructor to prform cleanup
## it is called by Python virtual machine

class Test:
	def __init__(self):
		print('object Initializatio...')
	def __del__(self):
		print('Fulfiling last wish and performing cleanup activities ...')
t1=Test()
	
	'''ex1
	t1=None
	#now t1 is not refring to any object so GC will  be called and t1 
	ex2'''
time.sleep(30)## in this case it is not applicable to For GC
print('end of Application')## destructor will be called automatically at the last

'''output
object Initializatio...
end of Application
Fulfiling last wish and performing cleanup activities ...
'''
t2=t1
t3=t2
t4=t3

# there are one object and 4 reference variable
#even if i delete t del t1 object will not be destroyed , object will be destroyed only when all the four refrence varible is deleted
list = [test(),test(),test()]
time.sleep(10)
list=None
time.sleep(10)
print('end of application')
# the destructor will be called thrice
''' Output

object Initializatio...
object Initializatio...
object Initializatio...
#wait for 10 seconds

Fulfiling last wish and performing cleanup activities ...
Fulfiling last wish and performing cleanup activities ...
Fulfiling last wish and performing cleanup activities ...
#Wait for 10 seconds
end of application
'''

print(sys.getrefcount(t1)) ##it will tell how many refrences are there 5(4+1(self-python implicit variable)) 





