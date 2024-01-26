import copy 

def can_bomb(consec, m):
    return any(count >= m- 1 for count in consec)

def get_consec(grid, col):
    n = len(grid)

    cnt = 0
    consec = [0] * n
    for i in range(n-1, 0, -1):
        if grid[i][col] == grid[i-1][col]:
            cnt += 1
        else:
            cnt = 0    
        consec[i] = cnt

    return consec

def bomb(grid, col, m, consective_lst):
    for idx, cnt in enumerate(consective_lst):
        if cnt >= m - 1:
            for i in range(idx-1, idx + cnt):
                grid[i][col] = 0 
    
def drop(grid):
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


def shift(grid):
    n = len(grid)
    tmp = copy.deepcopy(grid)

    # 90도 시계방향 회전
    for col in range(n):
        for row in range(n):
            grid[row][col] = tmp[n-col-1][row]

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
    for _ in range(k):
        for i in range(n):
            consecutive_lst = get_consec(grid, i)
            if can_bomb(consecutive_lst, m):
                bomb(grid, i, m, consecutive_lst)
        
        drop(grid)
        shift(grid)
        drop(grid)

    
    for i in range(n):
        consective_lst = get_consec(grid, i)
        
        if can_bomb(consective_lst, m):
            bomb(grid, i, m, consecutive_lst)
        
        drop(grid)
        shift(grid)
        drop(grid)

    result = check_bomb_cnt(grid)
    print(result)


solution()