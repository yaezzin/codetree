n, k = map(int, input().split())
lst = [int(input()) for i in range(n)]

bomb = [0] * 1000001

for i in range(n):
    max_cnt = 0
    for j in range(i+1, n):
        if lst[i] == lst[j] and j - i <= k:
            bomb[lst[i]] += 1

max_cnt = max(bomb)

answer = 0
for i in range(len(bomb)):
    if bomb[i] == max_cnt and bomb[i] != 0:
        answer = i
        break

print(answer)