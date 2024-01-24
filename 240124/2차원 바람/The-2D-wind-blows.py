n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

def pirnt_grid():
    for g in grid:
        print(*g)

def calculate_avg(x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    s = grid[x][y]
    c = 1
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if in_range(new_x, new_y):
            s += grid[new_x][new_y]
            c += 1
    
    return s // c

def move_right(r1, c1, r2, c2):
    for i in range(c2-1, c1-1, -1):
        grid[r1-1][i] = grid[r1-1][i-1]

def move_left(r1, c1, r2, c2):
    for i in range(c1, c2):
        grid[r2-1][i-1] = grid[r2-1][i]

def move_up(r1, c1, r2, c2):
    for i in range(r1-1, r2-1):
        grid[i][c1-1] = grid[i+1][c1-1]

def move_down(r1, c1, r2, c2):
    for i in range(r2-1, r1-1, -1):
        grid[i][c2-1] = grid[i-1][c2-1]

def shift(r1, c1, r2, c2):  
    tmp1 = grid[r1-1][c1-1]

    move_up(r1, c1, r2, c2)
    move_left(r1, c1, r2, c2)
    move_down(r1, c1, r2, c2)
    move_right(r1, c1, r2, c2)
    grid[r1-1][c1] = tmp1

if q == 0:
    pirnt_grid()
    
for _ in range(q):
    # 입력
    r1, c1, r2, c2 = map(int, input().split())

    # 시계방향으로 한칸씩 shift
    shift(r1, c1, r2, c2)

    # 평균 계산
    tmp_lst = [[0] * m for _ in range(n)]
    for i in range(r1-1, r2):
        for j in range(c1-1, c2):
            tmp_lst[i][j] = calculate_avg(i, j)
    
    for i in range(r1-1, r2):
        for j in range(c1-1, c2):
            grid[i][j] = tmp_lst[i][j]

    pirnt_grid()