# if user and pw exist return "Welcome Master" otherwise return "INTRUDER ALERT"

users = {
    "apple": "red",
    "lettuce": "green",
    "lemon": "yellow",
    "orange": "orange"
}
username = input("Please write your username ")
print("Thank you")
pw = input("Now, please write your password ")

try:
    if users[username] == pw:
        print("Welcome Master")
    else:
        print("INTRUDER ALERT")
except KeyError:
    print("INTRUDER ALERT")

"""
Uri's comments:
==============

* Very good! This code works.
* It's better not to write `print("INTRUDER ALERT")` twice. You can use either
  `users.get(username)` or `username in users` to check username without an exception,
  which is better in this case.

"""
