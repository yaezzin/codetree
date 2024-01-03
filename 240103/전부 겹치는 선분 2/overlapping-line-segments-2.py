import sys

n = int(input())

lst = [ list(map(int, input().split())) for _ in range(n)]

flag = 0
for i in range(n):
    max_x1 = 0
    min_x2 = sys.maxsize
    for j in range(n):
        if i == j:
            continue
        
        max_x1 = max(max_x1, lst[j][0])
        min_x2 = min(min_x2, lst[j][1])

    if max_x1 <= min_x2:
        flag = 1

if flag == 1:
    print('Yes')
else:
    print('No')