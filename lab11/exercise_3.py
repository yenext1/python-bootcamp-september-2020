# get text and return all if empty
text = []

user_input = input("Write me something...")
while user_input :
    text.append(user_input)
    user_input = input("Write me more...")


print("You wrote me such beautiful things:")
for t in text:
    print(t)

"""
Uri's comments:
==============

* This code works, but it doesn't print the lines in reverse order.
  
"""
