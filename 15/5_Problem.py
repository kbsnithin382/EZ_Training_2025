"""
given 2 strings
h7bw82b98rn8
mnd475nf982n49n
combine digits from each of those without duplicates => 782945
calculate the largest possible even number from it
"""

inp = input() + input()
s = set()

for i in inp:
    if i.isdigit():
        s.add(i)

s = list(map(int, list(s)))
s.sort(reverse = True)

for i in range(len(s)-1, -1 , -1):
    if s[i] % 2 == 0:
        s.append(s.pop(i))
        break

if s[-1] % 2 == 0:
    print(''.join(s))
else:
    print(-1)