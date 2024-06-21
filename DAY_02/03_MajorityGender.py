# Majority Gender

s = input().upper()
m = 0
for i in s:
    if i == 'M':
        m += 1
    else:
        m -= 1

if m > 0:
    print('M')
elif m < 0:
    print('F')
elif m == 0:
    print("Equal")