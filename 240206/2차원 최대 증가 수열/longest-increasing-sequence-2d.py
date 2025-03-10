n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def solution(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
        
    max_cnt = 1
    for i in range(x+1, n):
        for j in range(y+1, m):
            if in_range(i, j) and grid[i][j] > grid[x][y]:
                max_cnt = max(max_cnt, solution(i, j) + 1)
    
    dp[x][y] = max_cnt
    
    return max_cnt

solution(0, 0)
print(dp[0][0])