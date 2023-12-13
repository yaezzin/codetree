from itertools import groupby

n = int(input())

lst = [0 for _ in range(201)]

tmp = 0
for _ in range(n):
    num, location = input().split()

    if location == 'R':
        for i in range(tmp, tmp + int(num) + 1):
            lst[i] += 1
        
        tmp = tmp + int(num)

    else:
        for i in range(tmp, tmp - int(num) - 1, -1):
            lst[i] += 1
        
        tmp = tmp - int(num)


cnt = 0
answer = 0
for i in range(len(lst)):
    if lst[i] >= 2:
        cnt += 1
    
    elif lst[i] < 2 and cnt != 0:
        answer += cnt - 1
        cnt = 0
    
print(answer)