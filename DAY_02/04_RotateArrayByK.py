# rotate the array to the right by k

s = input()
k = int(input()) % 26
n = len(s)

s = list(s)
for i in range(n):
    asc = ord(s[i])
    asc -= k
    if asc < 97:
        asc = 123 - (97 - asc)
    s[i] = chr(asc)
s = "".join(s)

print(s)
