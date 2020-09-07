# if can be divided by 7 return boom
num = input("Pick a number!")

while (int(num) % 7 != 0):
    num = input("Pick another number!")

print("BOOM!")
