n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def print_grid():
    for g in grid:
        print(*g)

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def bomb(x, y):
    # 1 ) dx, dy 정의
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # 2 ) 움직여야 하는 횟수
    move_cnt = grid[x][y] - 1
    
    # 3 ) 움직이기
    grid[x][y] = 0
    for dx, dy in zip(dxs, dys):
        for i in range(move_cnt):
            new_x = x + (dx * (i+1))
            new_y = y + (dy * (i+1))

            if in_range(new_x, new_y):
                grid[new_x][new_y] = 0
        
def drop():
    global grid

    tmp = [[0] * n for _ in range(n)]

    # 0이 아닌 것만 담아주기
    for col in range(n):
        tmp_idx = n - 1

        for row in range(n-1, -1, -1):
            if grid[row][col] != 0:
                tmp[tmp_idx][col] = grid[row][col]
                tmp_idx -= 1
    
    grid = tmp

    
bomb(r-1, c-1)
drop()
print_grid()


# 중력으로 숫자 떨구기