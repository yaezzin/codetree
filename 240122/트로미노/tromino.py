n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    return False

def func(x, y):
    dxss = [[0, -1], [-1, 0], [0, 0], [1, 0], [0, 1], [-1, 1]]
    dyss = [[1, 0], [0, -1], [-1, 1], [0, -1], [1, 0], [0, 0]]

    max_value = 0
    for dxs, dys in zip(dxss, dyss):
        s = grid[x][y]
        
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            
            if in_range(new_x, new_y):
                s += grid[new_x][new_y]
        
        
        max_value = max(max_value, s)
    
    return max_value

answer = 0
for i in range(n):
    for j in range(m):
        result = func(i, j)
        answer = max(result, answer)

print(answer)