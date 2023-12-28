x, y = map(int, input().split())

cnt = 0
for n in range(x, y+1):
    n = str(n)
    
    if n == n[::-1]:
        cnt += 1

print(cnt)