import sys

INT_MAX = sys.maxsize
MAX_R = 100

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def init():
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX

    dp[0][0] = grid[0][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], grid[0][i])

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], grid[i][0])
    

    
def solution(lower_bound):
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lower_bound:
                grid[i][j] = INT_MAX

    init()

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])
    
    return dp[n-1][n-1]


answer = INT_MAX
for lower_bound in range(1, MAX_R + 1):
    upper_bound = solution(lower_bound)

    if upper_bound == INT_MAX:
        continue
    
    answer = min(answer, upper_bound - lower_bound)

print(answer)