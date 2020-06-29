#lecture19FileHandling:
###################################
'''
	permanently for the future purpose

	temporary storage areas: as long as program is executing we need the data to be stored.
	example : List,Tupe,dict,set  insdie pvm as the part of heap

	permanent storage areas: files and database concepts
	files -less information
	database concept: for large storage 
	Big data

	files:
	-----------------
	1. test files===> test data like names of students , marks of students etc
	2. Binary files---> images , video files, audio files etc

	Write/Read --------Opening of that file

	open(filename,mode)	#default mode is always read mode only

	to open abc.txt file for write operation 
	f=open('abc.txt','w')
	the allowed modes in python :
	--------------------------------------
	rwa=read wrtie append
	1. r---read 
		f=open('abc.txt','r')

		if the specified file is not available then we will get FileNotFoundError
	2. w----write
		f=open('abc.txt','w')
		if the specified is not available then this line will create that file
		if the file already contains some data ....it will perfom an overwrite operation
 
	3. a----append
		f=open('abc.txt','a')
		if the specified is not available then this line will create that file
		if the file already contains some data..it will append the data
	4. r+ ----read and write
	 	to read and then write
	5. w+ -----write and then read operation

	6. a+ ----- append and read
		first append and then read operation it will not overwrite the existing data

	7. x-  exclusive mode
	it is for write operation
	f=open('abc.txt','x')
	compulsory file should not be available
	if the file name is available then FileExistError
	--------------------------------------------------------
	r,w,a,r+,w+,a+,x
	for Binary fies ..........7 modes are available, and every modes end with b
	rb,wb,ab,r+b,w+b,a+b,xb
	f.close()#close the file after performing required operation

	f = open('abc.txt',r)
	-------------------------------
	various properties of file object:
	-----------------------------------
	f.names		 
	f.modes    		variables
	f.closed
	f.readable()
	f.writable()	methods


f=open('abc.txt','w')
print('file name',f.name)
print('file mode',f.mode)
print('file readable?',f.readable())
print('file writable?',f.writable())
print('file closed?',f.closed)
f.close()
print('file closed?',f.closed)

write data to file:
----------------------
f.write(str)
f.writelines(list of lines)

f=open('abc.txt','w')
f.write('Youtube\n')
f.write('Software\n')
f.write('Solutions\n')


l=['sunny\n','bunny\n','chinny\n','vinny\n']
f.writelines(l)
f.close()
print('Write Operation completed')

write some data to some file?

file name i will pass as dynamic input
data can be entered as dynamic iput

F:\input folder

fname=input('enter file name :')
f = open('path'+fname,'w')
feedback=input('Enter your feedback data:')
f.write(feedback)
f.close()

'''
'''
f.read()===to read total data from the file
f.read(n)====read n character from the file
f.readline()=====to read only one line
f.readlines()===to read al lines into a list

'''
'''
f = open('cmiabc.txt')
data = f.read(3)
print(data)
line=f.readline()
print(line,end='')

line=f.readline()
print(line,end='')

line=f.readline()
print(line)

'''
##to read all lines
f = open('cmiabc.txt')
lines=f.readlines()
for line in lines:
	print(line,end='')

with open('abc.txt','w') as f:
	f.write('svban')

























