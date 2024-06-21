# count the number of buildings that can get sunlight in the morning and evening based on their heights

heights = list(map(int, input().split()))

morning = 0
left = 0
for i in heights:
    if left < i:
        left = i
        morning += 1

evening = 0
right = 0
for i in heights[::-1]:
    if right < i:
        right = i
        evening += 1

print("morning access =", morning)
print("evening access =", evening)

