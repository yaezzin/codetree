MAX = 1000000

n, k = map(int, input().split())
lst = [int(input()) for i in range(n)]

bomb = [0] * (MAX + 1)
for i in range(n):
    for j in range(i+1, n):
        if lst[i] == lst[j] and j - i <= k:
            bomb[lst[i]] += 1

max_cnt = max(bomb)
answer = 0
for i in range(len(bomb)-1, -1, -1): # 거꾸로 도는 이유는 인덱스가 큰걸로 정답을 내야되기 때문에
    if bomb[i] == max_cnt and bomb[i] != 0:
        answer = i
        break

print(answer)