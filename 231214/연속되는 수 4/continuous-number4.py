n = int(input())
lst = [ int(input()) for _ in range(n) ]

m = 1
cnt = 1
for i in range(1, n):
    if lst[i-1] < lst[i]:
        cnt += 1
    else:
        cnt = 1
    
    m = max(cnt, m)

if m == 1:
    print(cnt)
else:
    print(m)