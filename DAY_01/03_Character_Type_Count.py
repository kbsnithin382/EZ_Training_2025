# count upper-case, lower-case vowels and consonants
# also count number of digits and special characters

s = input()

vowels = ['a', 'e', 'i', 'o', 'u']
lv = uv = uc = lc = d = sp = 0

for i in s:
    if i.isdigit():
        d += 1
    elif i.islower():
        if i in vowels:
            lv += 1
        else:
            lc += 1
    elif i.isupper():
        if i.lower() in vowels:
            uv += 1
        else:
            uc += 1
    else:
        sp += 1

print("UpperCase Vowels =", uv)
print("LowerCase Vowels =", lv)
print("UpperCase Consonants =", uc)
print("LowerCase Vowels =", lc)
print("Digits =", d)
print("Special Characters =", sp)