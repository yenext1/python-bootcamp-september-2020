# get 10 nums, return max
num_arr = []
for i in range(10):
    if i == 5:
        print("Half way there...")
    num = int(input(f"Choose a number ({i+1}/10)"))
    num_arr.append(num)


def return_max(numbers):
    largest_num = 0
    for n in numbers:
        if n > largest_num:
            largest_num = n
    # print(f"The largest number is {max(numbers)}")
    return largest_num


print (f"The largest number is: {return_max(num_arr)}")

"""
Uri's comments:
==============

* Very good! This code works.
* Python has the function "max", and it's better to use it than implementing
  your own solution.
  
"""
