#1.Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7.
# Make sure to use only higher order function.

def multiple(x):
	return True if x % 3 != 0 and x % 7 ==0 else False

print(multiple(40))
print(multiple(7))