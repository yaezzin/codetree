def func(n):
    if dp[n] != -1:
        return dp[n]

    if n < 2:
        dp[n] = 1

    else:
        dp[n] = func(n-1) + func(n-2)
    
    return dp[n]


n = int(input())
dp = [-1] * (n + 1)
print(func(n))