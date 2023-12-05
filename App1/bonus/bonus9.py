'''
Strong Password:
    1. 8 characters +
    2. at least one digit
    3. at least one upper case letter

'''

res = {}

password = input("Enter new password: ")
if len(password) >= 8:
    res['lence'] = True
else:
    res['lence'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
res['digit'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
res['uppercase'] = uppercase

if all(res):
    print("Strong Password")
else:
    print("Weak password")