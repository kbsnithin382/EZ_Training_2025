# calculate the next palindrome if the given number is not

s = input()

res = ""
index = 0
while len(res) < (len(s) // 2):
    res += s[index]
    index += 1
if len(s) % 2 == 1:
    res += s[index]

if s == s[::-1]:
    print(s)
else:
    res = int(res)
    res += 1
    res = str(res)

    if len(s) % 2 == 1:
        res += res[-2::-1]
    else:
        res +=  res[::-1]

    print(res)
