n = int(input())

lst = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    lst.append([name, int(height), int(weight)])

lst.sort(key=lambda x: x[1])

for l in lst:
    name, height, weight = l
    print(name, height, weight)