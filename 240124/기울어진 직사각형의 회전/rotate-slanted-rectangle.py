n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * n for _ in range(n)]
row, col, m1, m2, m3, m4, direction = list(map(int, input().split()))

def print_grid():
    for s in grid:
        print(*s)

def shift(x, y, k, l, d):
    if d == 0: 
        dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
        moves = [k, l, k, l]
    
    else:
        dxs, dys = [-1, -1, 1, 1], [-1, 1, 1, -1]
        moves = [l, k, l, k]

    # tmp에 grid 배열 복사
    for i in range(n):
        for j in range(n):
            tmp[i][j] = grid[i][j]

    # 움직이기
    for dx, dy, move in zip(dxs, dys, moves):
        for _ in range(move):
            nx, ny = x + dx, y + dy
            tmp[nx][ny] = grid[x][y]
            x, y = nx, ny
    
    # tmp값을 grid에 넣기
    for i in range(n):
        for j in range(n):
            grid[i][j] = tmp[i][j]


shift(row-1, col-1, m1, m2, direction)
print_grid()