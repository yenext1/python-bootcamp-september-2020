# get 3 numbers and return the largest

num1 = int(input("Can you choose a number?"))
num2 = int(input("Great! Now another one"))
num3 = int(input("Choose a last one..."))

larger_num = num1 if num1 > num2 else num2
largest_num = num3 if num3 > larger_num else larger_num

print(f"{largest_num} is the largest number")

"""
Uri's comments:
==============

* Very good! This code works.
* This is sub-exercise 5.
* Python has the function "max", and it's better to use it than implementing
  your own solution. You don't have to "invent the wheel" each time again.
  Built-in Functions in Python: https://docs.python.org/3/library/functions.html
* It's better to end a Python file with a line break.
  If you use PyCharm's Code -> Reformat Code feature, it will be done automatically.
  This is relevant to all your exercises.
  
"""
