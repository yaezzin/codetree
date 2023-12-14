n = int(input())

lst = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    lst.append([name, int(height), int(weight)])

lst.sort(key=lambda x: x[1])

for name, height, weight in lst:
    print(name, height, weight)