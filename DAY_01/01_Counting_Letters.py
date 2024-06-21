# given a string => aaabbcd
# output => a3b2c1d1

s = input()

i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j] == s[i]:
        j += 1
    s = s[:i+1] + str(j-i) + s[j:]
    i = j

print(s)
