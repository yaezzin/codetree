n, m = map(int, input().split())

lst = []
for _ in range(m):
    a, b = map(int, input().split())
    lst.append([min(a,b), max(a,b)])

max_cnt = 0
for i in range(len(lst)):
    cnt = 1
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)