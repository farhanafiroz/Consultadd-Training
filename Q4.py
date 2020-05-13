#4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also.

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
dictionary = dict(zip(Student, capital))
print (dictionary)