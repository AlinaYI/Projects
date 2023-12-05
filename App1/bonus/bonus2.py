"""
check the user type the correct password
"""

password = input("Enter your password: ")

while password != "pass123":
    print("Wrong password")
    password = input("Enter your password: ")

print("Password was correct!! Welcome to the system")