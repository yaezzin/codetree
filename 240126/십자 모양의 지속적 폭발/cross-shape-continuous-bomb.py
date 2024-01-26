def print_grid(grid):
    for g in grid:
        print(*g)

def shift(grid):
    n = len(grid)

    for col in range(n):
        tmp = [0] * n
        tmp_idx = n - 1

        for row in range(n-1, -1, -1):
            if grid[row][col] != 0:
                tmp[tmp_idx] = grid[row][col]
                tmp_idx -= 1
     
        for row in range(n-1, -1, -1):
            grid[row][col] = tmp[row]

            
def in_range(x, y, n):
    return x >= 0 and y >= 0 and x < n and y < n

def remove(x, y, grid):
    n = len(grid)
    s = grid[x][y]

    dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]    
    for dx, dy in zip(dxs, dys):
        for i in range(s):
            nx = x + (dx * i)
            ny = y + (dy * i)

            if in_range(nx, ny, n):
                grid[nx][ny] = 0 

def find_row(col, grid):
    for row in range(len(grid)):
        if grid[row][col] != 0:
            return row
    return -1

def solution():
    n , m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    col = [int(input()) for _ in range(m)]
    
    # 계속 두번쨰 열을 선택했을 때 0 이 아닌 구간부터 시작! 
    for c in col:
        r = find_row(c-1, grid)
        
        if r == -1:
            continue

        remove(r, c-1, grid)
        shift(grid)

    print_grid(grid)


solution()