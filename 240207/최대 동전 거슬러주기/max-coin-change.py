n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (m + 1)
for i in range(1, m + 1):
    for j in range(n):
        if i >= coins[j]:
            dp[i] = max(dp[i], dp[i-coins[j]]+ 1)

print(dp[m])