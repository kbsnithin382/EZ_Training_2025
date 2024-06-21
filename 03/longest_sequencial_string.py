# length of longest sequential string

s = input()
n = len(s)

s = list(s)
count = 1
max_count = count
for i in range(1, n):
    if ord(s[i]) == (ord(s[i-1]) + 1):
        count += 1
    else:
        max_count = max(max_count, count)
        count = 1

print(max_count)
