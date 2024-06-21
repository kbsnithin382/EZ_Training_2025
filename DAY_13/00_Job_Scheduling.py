
time = [(1,3), (2,5), (4,6), (6,7), (5,8), (7,9)]
profit = [5, 6, 5, 4, 11, 2]


n = len(time)

for i in range(n-1):
    for j in range(n-1-i):
        if time[j][1] < time[j+1][1]:
            time[j], time[j+1] = time[j+1], time[j]
            profit[j], profit[j+1] = profit[j+1], profit[j]

profits = profit[:]
for i in range(n):
    for j in range(i):
        if time[i][0] >= time[j][1]:
            tot = profit[i] + profits[j]
            if tot > profits[i]:
                profits[i] = tot
print(max(profits))