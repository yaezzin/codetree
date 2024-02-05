n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
def init():
    dp[0][0] = lst[0][0]

    for i in range(1, n):
        dp[0][i] = max(lst[0][i], dp[0][i-1])

    for i in range(1, n):
        dp[i][0] = max(lst[i][0], dp[i-1][0])
    
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(max(lst[i][j], dp[i-1][j]), max(lst[i][j], dp[i][j-1]))

init()
print(dp[n-1][n-1])