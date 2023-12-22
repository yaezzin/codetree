n, m = map(int, input().split())
lst = list(map(int, input().split()))
sub = sorted(list(map(int, input().split())))

cnt = 0
for i in range(n-m+1):
    tmp = sorted(lst[i:i+m])

    if tmp == sub:
        cnt += 1

print(cnt)