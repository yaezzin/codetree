GRID_LEN = 4

def push_U(grid):
    # 중력으로 올린다
    for col in range(GRID_LEN):
        tmp = [0] * GRID_LEN
        tmp_idx = 0

        for row in range(GRID_LEN):
            if grid[row][col] != 0:
                tmp[tmp_idx] = grid[row][col]
                tmp_idx += 1 
    
        for i in range(len(tmp)):
            grid[i][col] = tmp[i]

    # 합친다
    for col in range(GRID_LEN):
        for row in range(GRID_LEN-1):
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] = grid[row][col] * 2
                grid[row+1][col] = 0

            elif grid[row][col] != grid[row+1][col]:
                # 숫자가 다르고 내가 0 이라면
                if grid[row][col] == 0:
                    grid[row][col] = grid[row+1][col]
                    grid[row+1][col] = 0

def push_D(grid):
    # 중력으로 내린다
    for col in range(GRID_LEN):
        tmp = [0] * GRID_LEN
        tmp_idx = GRID_LEN - 1

        for row in range(GRID_LEN-1, -1, -1):
            if grid[row][col] != 0:
                tmp[tmp_idx] = grid[row][col]
                tmp_idx -= 1 
    
        for i in range(len(tmp)):
            grid[i][col] = tmp[i]
        
    # 합친다
    for col in range(GRID_LEN):
        for row in range(GRID_LEN - 1, 0, -1):
            if grid[row][col] == grid[row-1][col]:
                grid[row][col] = grid[row][col] * 2
                grid[row-1][col] = 0

            elif grid[row][col] != grid[row-1][col]:
                # 숫자가 다르고 내가 0 이라면
                if grid[row][col] == 0:
                    grid[row][col] = grid[row-1][col]
                    grid[row-1][col] = 0

def push_R(grid):
    # 중력으로 떨군다
    for row in range(GRID_LEN):
        tmp = [0] * GRID_LEN
        tmp_idx = GRID_LEN -1

        for col in range(GRID_LEN - 1, -1, -1):
            if grid[row][col] != 0:
                tmp[tmp_idx] = grid[row][col]
                tmp_idx -= 1
            
        grid[row] = tmp
    

    # 더한다
    for row in range(4):
        for col in range(4-1, 0, -1):
            if grid[row][col] == grid[row][col-1]:
                grid[row][col] = grid[row][col] * 2
                grid[row][col-1] = 0

            elif grid[row][col] != grid[row][col-1]:
                # 숫자가 다르고 내가 0 이라면
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col-1]
                    grid[row][col-1] = 0

def push_L(grid): 
    # 중력으로 떨군다
    for row in range(GRID_LEN):
        tmp = [0] * GRID_LEN
        tmp_idx = 0

        for col in range(GRID_LEN):
            if grid[row][col] != 0:
                tmp[tmp_idx] = grid[row][col]
                tmp_idx += 1
            
        grid[row] = tmp
    
    # 더한다
    for row in range(GRID_LEN):
        for col in range(GRID_LEN-1):
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] = grid[row][col] * 2
                grid[row][col+1] = 0

            elif grid[row][col] != grid[row][col-1]:
                # 숫자가 다르고 내가 0 이라면
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col+1]
                    grid[row][col+1] = 0


def solution():
    grid = [list(map(int, input().split())) for _ in range(4)]
    direction = input()

    if direction == 'R':
        push_R(grid)
    
    elif direction == 'L':
        push_L(grid)
    
    elif direction == 'U':
        push_U(grid)
    
    else:
        push_D(grid)
    
    for g in grid:
        print(*g)

solution()