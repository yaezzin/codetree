import sys
INT_MIN = -sys.maxsize

n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n

for i in range(1, len(dp)):
    dp[i] = INT_MIN

for i in range(1, n):
    for j in range(i):
        # 도달이 불가능한 경우를 위해 넣어줘야함
        if lst[j] == INT_MIN:
            continue

        if lst[j] + j >= i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))