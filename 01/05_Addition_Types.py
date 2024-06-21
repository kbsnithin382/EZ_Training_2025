
s = list(map(float, input().split()))

even_sum = 0
odd_sum = 0
decimal_sum = 0
for i in s:
    if str(s) != str(int(s)):
        decimal_sum += i
    elif i % 2 == 0:
        even_sum += int(i)
    else:
        odd_sum += int(i)

print("Even Sum =", even_sum)
print("Odd Sum =", odd_sum)
print("Decimal Sum =", round(decimal_sum, 2))