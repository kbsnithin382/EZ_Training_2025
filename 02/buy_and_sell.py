
l = list(map(int, input().split()))

max_profit = 0
buy = l[0]
for i in l:
    if i < buy:
        buy = i
    profit = i - buy
    max_profit = max(max_profit, profit)

print(max_profit)

