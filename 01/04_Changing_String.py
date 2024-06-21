
s = list(input())

vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(s)):
    if s[i].lower() in vowels:
        s[i] = s[i].upper()
    else:
        s[i] = s[i].lower()
s = "".join(s)

print(s)