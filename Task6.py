#1.Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7.
# Make sure to use only higher order function.

def multiple(x):
	return True if x % 3 != 0 and x % 7 ==0 else False

print(multiple(40))
print(multiple(7))

#2.Write a program in Python to multiple the element of list by itself using traditional function and pass
# the function to map to complete the operation.

numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x * x, numbers)
print(list(result))

#3.Write a program to Python find out the character in a string which is uppercase using list comprehension.

test_str = "ConsultAdd"
print ("The original string is : " + str(test_str))
res = [char for char in test_str if char.isupper()]
print ("The uppercase characters in string are : " + str(res))

#4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also.

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
dictionary = dict(zip(Student, capital))
print (dictionary)

#8.Learn about What is FRONT END and its Technologies and Tools.

#In the world of software development, what’s built falls into two categories:
#everything that’s seen by the user and the processes happening in the background.
#What we see and interact with as the visitors of a website, or as the end user of a mobile app, is considered front-end technology.
#These are 5 top notch technologies of Frontend.

#1.	HTML,
#2.	CSS,
#3.	JavaScript- Facebook, YouTube, MSN, Amazon.
#4.	Angular-Google.
#5.	React