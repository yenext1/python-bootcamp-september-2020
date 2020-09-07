# get 3 numbers and return the largest

num1 = int(input("Can you choose a number?"))
num2 = int(input("Great! Now another one"))
num3 = int(input("Choose a last one..."))

larger_num = num1 if num1 > num2 else num2
largest_num = num3 if num3 > larger_num else larger_num

print(f"{largest_num} is the largest number")