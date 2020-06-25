#Abstract class 
#python does not support abstract class however we can define ABC

from abc import ABC,abstractmethod
#abc stands abstact base class
class Computer(ABC):
	@abstractmethod
	def Process(self):
		pass
	#Abstact method which has declartion but not a definition.
	#and a class which has abstract method is known as abstact class
	#but python does not support but we have ABC module

class Laptop(Computer):
	#pass but it won't work
	def Process(self):
		print('Process running)
class whiteboard(Computer):
	def write(self):
		print('its writing')
class Programmer:
	def Work(self):
		print('solving Bug')

#com=Computer()
lap=Laptop()
#com.Process()



#example
from abc import ABC, abstractmethod

class Animal(ABC):
	@abstactmethod  #to make abstract class we must import predefined
	def move(self):
		psss

class Human(Animal):
	
	def move(self):
		print('i can walk')
	
class Snake(Animal):
	def move(self):
		print('i can crawl....)

def main():
	#for abstact class we don not create object of Abstact class otherwise it will show an error
	#however there is no decrator we can create object then.
	h1=Human()
	h1.move()
	
	s1=Snake()
	s1.move()
if __name__== "__main__()":
	main()