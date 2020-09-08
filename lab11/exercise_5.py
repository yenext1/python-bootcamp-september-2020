# get rand num (1,1M) and return if can be divided by 7,13,and 15
from random import randint
n1 = randint(1,10)
n2 = randint(1,10)
print(f"N1 is {n1}, N2 is {n2}")
for i in range(n1*n2):
    num = i+1
    if (num % n1 + num % n2 == 0):
        print(f"The smallest multiplpliable number is {num}")
        break
