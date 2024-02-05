n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


def init():
    dp[0][0] = lst[0][0]

    # 첫번쨰 행 초기화
    for i in range(1, n):
        dp[0][i] = min(dp[0][i-1], lst[0][i])

    # 첫번째 열 초기화
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], lst[i][0])

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i-1][j], lst[i][j]), min(dp[i][j-1], lst[i][j]))
    
    print(dp[n-1][n-1])

init()