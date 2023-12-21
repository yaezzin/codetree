n, m = map(int, input().split())
lst = [[0] * m for _ in range(n)]
lst[0][0] = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def solution():
    # 아래 왼쪽 위 오른쪽 
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    cur_dir = 0
    x, y = 0, 0
    
    for i in range(2, n * m + 1):
        nx = x + dx[cur_dir]
        ny = y + dy[cur_dir]

        if not in_range(nx, ny) or lst[nx][ny] != 0:
            cur_dir = (cur_dir - 1 + 4) % 4
        
        x = x + dx[cur_dir]
        y = y + dy[cur_dir]

        lst[x][y] = i

    for i in range(n):
        for j in range(m):
            print(lst[i][j], end =' ')
        print()

solution()