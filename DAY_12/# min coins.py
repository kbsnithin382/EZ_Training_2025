# min coins

coins = list(map(int, input().split()))
amount = int(input())

coins.sort(reverse = True)
count = 0
i = 0
while amount:
    count += amount // coins[i]
    amount %= coins[i]
    i += 1

print(count)

