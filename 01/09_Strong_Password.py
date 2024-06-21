
upper = False
lower = False
digit = False
special = False

password = input()
for i in password:
    if i.isdigit():
        digit = True
    elif i.isupper():
        upper = True
    elif i.islower():
        lower = True
    else:
        special = True

req = 0
if digit == False:
    req += 1
if upper == False:
    req += 1
if lower == False:
    req += 1
if special == False:
    req += 1
if len(password) < 8 and (8 - len(password)) > req:
    req = 8 - len(password)

if req == 0:
    print(-1)
else:
    print(req)