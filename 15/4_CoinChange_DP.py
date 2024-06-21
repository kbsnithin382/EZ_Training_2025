# check if given amount of money can be formed using given coins (only one unit of each coin)
# dp

coins = list(map(int, input().split()))
amount = int(input())

line = [0 for i in range(amount+1)]
line[0] = 1

visited = []
for i in coins:
    line[i] = 1
    for j in range(i+1, amount+1):
        if line[j] != 1:
            if line[amount-i] == 1:
                line[j] = 1

print(line)
