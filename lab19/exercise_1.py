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
