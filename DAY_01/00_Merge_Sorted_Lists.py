# given two sorted lists, merge them in sorted order

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list3 = []

# Merge Sort Algo
i = j = 0
while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        list3.append(list1[i])
        i += 1
    else:
        list3.append(list2[j])
        j += 1
list3 += list1[i:] + list2[j:]

print(list3)