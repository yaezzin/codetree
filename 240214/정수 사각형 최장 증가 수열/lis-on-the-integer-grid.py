n = int(input())

grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]

dp = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def solution(x, y, move_cnt):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    max_move_cnt = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            max_move_cnt = max(max_move_cnt, solution(nx, ny, move_cnt) + 1)
        
    dp[x][y] = max_move_cnt
    
    return max_move_cnt
    
answer = 0
for i in range(n):
    for j in range(n):
        tmp = solution(i, j, 1)
        answer = max(answer, tmp)

print(answer)