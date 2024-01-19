MAX = 1000
MOD = 10007

n = int(input())

dp = [0] * (MAX + 1)
dp[0], dp[2], dp[3] = 1, 1, 1
dp[1] = 0

for i in range(4, n + 1):
    dp[i] = dp[i-3] + dp[i-2] 
 
print(dp[n] % MOD)