n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n 

def func(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]  
    
    s = 0               
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy 
            
            if not in_range(x, y):
                return 0
            
            s += grid[x][y]

    return s

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                answer = max(answer, func(i, j, k, l))

print(answer)