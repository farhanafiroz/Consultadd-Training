#2. Write a program in Python to multiple the element of list by itself using traditional function and pass
# the function to map to complete the operation.

numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x * x, numbers)
print(list(result))

