print("Lets make a Arithmetic Progression!")
a1 = int(input("Choose the first number (a1)"))
d = int(input("Great! choose the number you and to add (d)"))
n = int(input("How many numbers should we sum? (n)"))

sum = (n/2)*(2*a1+(n-1)*d)

print(f" The sum of the numbers in the serie is {sum}")

"""
Uri's comments:
==============

* Very good! This code works.
* This is sub-exercise 6.
* "choose the number you and to add" is not the correct way to write in English.
* The input is done in int, but the result is in float. Maybe it's better to
  convert it to int (it can't be a non-integer number).
  You can also do the whole calculation in int to reserve precision (you lose 
  precision after the first ~15 digits when you convert an int to a float).
* sum is a built-in function in Python and although you can, it's not recommended
  to use it as a name of a variable.
  PyCharm warns about it (you can see a line under "sum" which you can hover and 
  see the full warning).
* There are 6 sub-exercises in exercise 5, and you only did 5 of them. 

"""
