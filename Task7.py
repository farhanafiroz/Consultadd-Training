#1.	Write a program that calculates and prints the value according to the given formula:
#Q= Square root of [(2*C*D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.

import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)

#2.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(5)
print (aSquare.area())

#3.Create a class to find the three elements that sum to zero from a set of n real numbers.
#Input array: [-25,-10,-7,-3,2,4,8,10]
#Output: [[-10,2,8],[-7,-3,10]]

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

#4.What is the output of the following code? Explain your answer as well.

class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        super().__init__() #( This line has added)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

#Output: 0 1
#Explanation:When main() function is called, object b of Derived_Test class is created which also inherits the properties of Test class.

class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main() #(There was a syntax error)

#Output: 1 2

class A:
    def __init__(self, x):
        self.x = x

    def count(self, x):
        self.x = self.x + 1

class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y

    def count(self,y):
        self.y += 1

def main():
    obj = B()
    obj.count()

    print(obj.x, obj.y)

main()

#Output:

#Traceback (most recent call last):
 # File "/Users/onna/Desktop/Consultadd_training/Question4.py", line 22, in <module>
  #  main()
  #File "/Users/onna/Desktop/Consultadd_training/Question4.py", line 18, in main
   # obj.count()
#TypeError: count() missing 1 required positional argument: 'y'

class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i;

class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i;

obj = B()

#Output: 30

#Create a Time class and initialize it with hours and minutes.
#Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min).
#Make a method displayTime which should print the time.
#Make a method DisplayMinute which should display the total minutes in the Time.

class Time(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(t1, t2):
        t3 = Time(0, 0)
        t3.hours = t1.hours + t2.hours
        t3.minutes = t1.minutes + t2.minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3

    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours, self.minutes))

    def displayMinutes(self):
        print((self.hours * 60) + self.minutes, "minutes")

a = Time(2, 90)
b = Time(1, 90)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinutes()

input()

#6 Maybe Question is not right.