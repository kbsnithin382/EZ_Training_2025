
uv = ['A', 'E', 'I', 'O', 'U']
lv = ['a', 'e', 'i', 'o', 'u']
lc = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
uc = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
d = []
for i in range(10):
    d.append(str(i))

cuv = 0
clv = 0
cuc = 0
clc = 0
cd = 0
cs = 0

str1 = input()
for i in str1:
    if i in uv:
        cuv += 1
    elif i in lv:
        clv += 1
    elif i in lc:
        clc += 1
    elif i in uc:
        cuc += 1
    elif i in d:
        cd += 1
    else:
        cs += 1

print("UpperCase Vowels =", cuv)
print("LowerCase Vowels =", clv)
print("UpperCase Consonants =", cuc)
print("LowerCase Vowels =", clc)
print("Digits =", cd)
print("Special Characters =", cs)