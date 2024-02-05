n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def init():
    dp[0][0] = lst[0][0]

    # 첫번째 행 초기화
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + lst[0][i]
    
    # 첫번째 열 초기화
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + lst[i][0]

    # 나머지 초기화
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + lst[i][j]

init()
print(dp[n-1][n-1])