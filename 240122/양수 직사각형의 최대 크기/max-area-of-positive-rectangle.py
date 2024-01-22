n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

def func(x, y):
    max_size = 0
    for row in range(n-x):
        for col in range(m-y):
            # 내 위치x,y부터 x+row, y+col까지 모든 영역에서 음수가 있는지 확인
            
            flag = 1
            for i in range(row + 1):
                for j in range(col + 1):
                    if in_range(x + i, y + j):
                        if grid[x + i][y + j] <= 0:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                if not flag:
                    break

            if flag: 
                max_size = max(max_size, (row + 1) * (col + 1)) 
    
    return max_size
                
        
answer = 0
for i in range(n):
    for j in range(m):
        result = func(i, j)
        answer = max(answer, result)

if answer == 0:
    print(-1)
else:
    print(answer)