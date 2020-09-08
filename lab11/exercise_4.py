# get rand num (1,1M) and return if can be divided by 7,13,and 15
from random import randint
num = randint(1,1000000)
while (num % 7 + num % 13 + num % 15 != 0):
    num = randint(1, 1000000)
else :
    print(f"The number {num} can be divided by 7, 13 and 15")

"""
Uri's comments:
==============

* Very good! This code works.
* Formatting - PEP-8 expects no spaces between "else" and ":". PyCharm warns
  about it.
  If you use PyCharm's Code -> Reformat Code feature, it will be done automatically.
  
"""
