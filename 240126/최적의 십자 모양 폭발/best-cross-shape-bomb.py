import copy

def in_range(x, y, n):
    return x >= 0 and y >= 0 and x < n and y < n 

def find_pair(grid):
    # 오른쪽, 아래만 정의하기
    n = len(grid)
    dxs, dys = [0, 1], [1, 0]
    
    cnt = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            current_num = grid[x][y]

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                
                if in_range(nx, ny, n) and current_num == grid[nx][ny] and current_num != 0 and grid[nx][ny] != 0:
                    cnt += 1
    
    return cnt 

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

    return grid

def bomb(x, y, grid):
    n = len(grid)
    size = grid[x][y]

    dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        for s in range(size):
            nx, ny = x + (dx * s), y + (dy * s)

            if in_range(nx, ny, n):
                grid[nx][ny] = 0
    
    return grid

def solution():
    # 입력
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 완전 탐색
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            # 이 위치에서 삭제한다
            bomb_grid = bomb(i, j, copy.deepcopy(grid))

            # 중력으로 내린다
            shift_grid = shift(bomb_grid)

            # 근접한 위치에 쌍이 몇개 있는지 확인한다.
            cnt = find_pair(shift_grid)

            # 최대값 갱신하기 
            max_cnt = max(max_cnt, cnt)
    
    # 출력
    print(max_cnt)

solution()