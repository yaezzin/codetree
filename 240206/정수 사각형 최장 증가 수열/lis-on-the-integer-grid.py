n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * n for _ in range(n)]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def solution(x, y, move_cnt):
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    
    max_move_cnt = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and lst[nx][ny] > lst[x][y]:
            max_move_cnt = max(max_move_cnt, solution(nx, ny, move_cnt) + move_cnt)
        
    memo[x][y] = max_move_cnt
    return max_move_cnt
    
answer = 0
for i in range(n):
    for j in range(n):
        tmp = solution(i, j, 1)
        answer = max(answer, tmp)

print(answer)