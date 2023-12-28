N = int(input())

h = [0] * 100
for i in range(1, N+1):
    h[i] = int(input())


max_cnt = 0
for i in range(1, 1001): 
    cnt = 1
    
    lst = []
    for j in range(1, N+1):
        if h[j] - i > 0:
            lst.append(j)

    for k in range(1, len(lst)):
        if abs(lst[k-1] - lst[k]) != 1:
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)