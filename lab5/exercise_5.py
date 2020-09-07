print("Lets make a Arithmetic Progression!")
a1 = int(input("Choose the first number (a1)"))
d = int(input("Great! choose the number you and to add (d)"))
n = int(input("How many numbers should we sum? (n)"))

sum = (n/2)*(2*a1+(n-1)*d)

print(f" The sum of the numbers in the serie is {sum}")