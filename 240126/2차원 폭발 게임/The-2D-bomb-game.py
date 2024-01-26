import copy

def can_bomb(consec, m):
    return any(count >= m - 1 for count in consec)

def get_consec(grid, col):
    n = len(grid)

    cnt = 0
    consec = [0] * n
    for i in range(n - 1, 0, -1):
        if grid[i][col] == grid[i - 1][col]:
            cnt += 1
        else:
            cnt = 0
        consec[i] = cnt

    return consec

def bomb(grid, col, m, consecutive_lst):
    for idx, cnt in enumerate(consecutive_lst):
        if cnt >= m - 1:
            for i in range(idx - 1, idx + cnt):
                grid[i][col] = 0

def drop(grid):
    n = len(grid)

    for col in range(n):
        tmp = [0] * n
        tmp_idx = n - 1
        for row in range(n - 1, -1, -1):
            if grid[row][col] != 0:
                tmp[tmp_idx] = grid[row][col]
                tmp_idx -= 1

        for row in range(n - 1, -1, -1):
            grid[row][col] = tmp[row]

def shift(grid):
    n = len(grid)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = rotated[i][j]

def check_bomb_cnt(grid):
    n = len(grid)
    cnt = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                cnt += 1
    return cnt

def solution():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # k번 반복하며 m개 이상인 것들은 폭발시킨다.
    for i in range(1001):
        flag = 0

        for i in range(n):
            consecutive_lst = get_consec(grid, i)
            if can_bomb(consecutive_lst, m):
                bomb(grid, i, m, consecutive_lst)
                flag = 1

        drop(grid)
        shift(grid)
        drop(grid)
        
        if flag == 0:
            break

    
        
    result = check_bomb_cnt(grid)
    print(result)

solution()