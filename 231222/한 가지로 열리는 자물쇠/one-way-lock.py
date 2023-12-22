n = int(input())
lst = list(map(int, input().split()))

# 전체 경우의 수
total = n * n * n

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if abs(i - lst[0]) > 2 and abs(j - lst[1]) > 2 and abs(k - lst[2]) > 2:
                #print(i, j, k)
                cnt += 1

print(total - cnt)