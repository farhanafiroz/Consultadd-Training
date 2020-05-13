#3.Write a program to Python find out the character in a string which is uppercase using list comprehension.

test_str = "ConsultAdd"
print("The original string is : " + str(test_str))
res = [char for char in test_str if char.isupper()]
print("The uppercase characters in string are : " + str(res))