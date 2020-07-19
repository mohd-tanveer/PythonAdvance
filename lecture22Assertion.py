#lecture22
#Assertions:
'''--------------------------
	assertion is use for DeBugging Purpose as an alternative of Print statements,
	if we are using print statement that should be remove after fixing the problem how ver aseert is not need to be executed based on choice we can enabled or disable the assertion statements.

#Type of assert statments:
----------------------------------
1. Simple Version
-----------------------
syntax:
	assert conditional_experession
		AssertionError

2. Augmented version
syntax:
	assert conditional_experession,'message'
		AssertionError

'''
#type1
'''
x=10
assert  x=810
print(x)

#type 2
x=10
assert x>10,'here x value should be > 10 but it is not'
print(x)
'''
def squareIt(x):
	return x**2

assert squareIt(2)==4,'the square of 2 should be 4'
assert squareIt(3)==9,'the square of 2 should be 9'
assert squareIt(4)==16,'the square of 2 should be 16'

print(squareIt(2))
print(squareIt(3))
print(squareIt(4))