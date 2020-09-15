# get 20 nums via command line than return average and all grades above average
import sys

grades = sys.argv[1:21]
while len(grades) < 20:
    grades = grades + (input(f"There are {len(grades)}/20 grades, Please add {20 - len(grades)} grades ").split())

avg = sum(map(int, (grades[0:20]))) / 20

print(f"The average grade is {avg}")
print("The following grades are higher than the average")
for grade in grades:
    if int(grade) > int(avg):
        print(grade)
