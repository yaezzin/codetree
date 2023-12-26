import sys

n = int(input())
lst = [ list(map(int, input().split())) for _ in range(n)]

min_value = sys.maxsize
for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            continue
            
        x = abs(lst[i][0] - lst[j][0])
        y = abs(lst[i][1] - lst[j][1])

        distance = x ** 2 + y ** 2
        min_value = min(min_value, distance)

print(min_value)