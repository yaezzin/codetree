def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 왼 아 오  위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(input())
lst = [[0] * n for _ in range(n)]

lst[n-1][n-1] = n * n

x, y = n-1, n-1
cur_dir = 0
for i in range(2, n * n + 1):
    
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]

    if not in_range(nx, ny) or lst[nx][ny] != 0:
        cur_dir = (cur_dir - 1 + 4) % 4
    
    x = x + dx[cur_dir]
    y = y + dy[cur_dir]

    lst[x][y] = (n * n) - i + 1

for i in range(n):
    for j in range(n):
        print(lst[i][j], end = ' ')
    print()