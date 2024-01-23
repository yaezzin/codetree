n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

wind = []
for _ in range(q):
    r, d = input().split()
    wind.append([int(r), d])

def move_left(row):   
    # 첫번쨰 원소 저장해놓기
    tmp = grid[row][0] 
    
    # 왼쪽으로 밀기
    for i in range(1, m):
        grid[row][i-1] = grid[row][i]

    grid[row][m-1] = tmp

def move_right(row):
    # 마지막 원소 저장해놓기
    tmp = grid[row][m-1] 
    
    # 오른쪽으로 밀기
    for i in range(m-1, 0, -1):
        grid[row][i] = grid[row][i-1]

    # 마지막 넣기
    grid[row][0] = tmp

def check_same_num(row, adj_row):
    # 같은 숫자가 하나라도 있으면 True
    for i in range(m):
        if grid[row][i] == grid[adj_row][i]:
            return True
    
    return False

def solution():
    for w in wind:
        row, direction = w 
        row -= 1

        # row를 direction 방향으로 우선 변경한다
        if direction == 'R':
            move_left(row)
        else:
            move_right(row)
    
        # row 위쪽을 변경한다
        flag = -1 if direction == 'L' else 1

        for i in range(row, 0, -1):
            if check_same_num(i, i-1):
                if flag == 1:
                    move_right(i-1)

                else:
                    move_left(i-1)
                
                flag = -flag
            
            else:
                break
            
        flag = -1 if direction == 'L' else 1

        # row 아래쪽을 변경한다.
        for i in range(row, n-1):
            if check_same_num(i, i+1):
                if flag == 1:
                    move_right(i+1)

                else:
                    move_left(i+1)
                
                flag = -flag
            
            else:
                break
     
    
solution()
for i in grid:
    print(*i)