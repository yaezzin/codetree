MAX_N = 1000

n = int(input())
dp = [0] * MAX_N

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n])