n = int(input())
grid = [input() for _ in range(n)]
start_num = int(input())

# 3 ) x, y에서 시작해서 next_dir방향으로 이동한 이후의 위치를 반환
def move(x, y, next_dir):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] # 아래, 왼, 위, 오른쪽

    nx, ny = x + dxs[next_dir], y + dys[next_dir]

    return nx, ny, next_dir

# 2 ) 범위 확인
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 1 ) 이동 가능한 만큼 계속 진행
def simulate(x, y, move_dir):
    move_num = 0

    while in_range(x, y):
        if grid[x][y] == '/': # 0 <-> 1 and 2 <-> 3
            x, y, move_dir = move(x, y, move_dir ^ 1)
        
        else: # 0 <=> 3 and 1 <=> 2
            x, y, move_dir = move(x, y, 3 - move_dir)

        move_num += 1
    
    return move_num

# 0 ) 초기 설정
def initialize(start_num):
    # 1 ~ n 범위라면 첫번째줄의 칸에서 아래방향
    if start_num <= n:
        return 0, start_num - 1, 0
    
    elif start_num <= 2 * n:
        return start_num - n -1, n - 1, 1
    
    elif start_num <= 3 * n:
        return n-1, n - (num -2 * n) , 2
    
    else:
        return n - (num -3 * n), 0, 3



### Main ###
x, y, move_dir = initialize(start_num)
move_num = simulate(x, y, move_dir)
print(move_num)