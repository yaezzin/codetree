# 8  3  1
# 9  11 2
# 10  19 11

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def print_dp():
    for d in dp:
        print(*d)

def init():
    dp[0][n-1] = lst[0][n-1] 

    # 첫번째 행 초기화
    for i in range(n-2, -1, -1):
        dp[0][i] = lst[0][i] + dp[0][i+1]

    # 마지막 열 초기화
    for i in range(1, n):
        dp[i][n-1] = lst[i][n-1] + dp[i-1][n-1]

    # 나머지 초기화
    for i in range(1, n):
        for j in range(n-2, -1, -1):
            dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + lst[i][j]

init()
print(dp[n-1][0])