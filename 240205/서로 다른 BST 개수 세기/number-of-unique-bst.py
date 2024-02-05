MAX_N = 1000

n = int(input())

dp = [0] * MAX_N
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    for j in range(n):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[n])