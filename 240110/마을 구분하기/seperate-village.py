def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y) or grid[x][y] == 0 or visited[x][y] == 1:
        return False
    else:
        return True

def dfs(x, y):
    global cnt

    visited[x][y] = 1
    cnt += 1

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    for dx, dy in zip(dxs, dys): 
        new_x = x + dx 
        new_y = y + dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)
    
    return cnt

n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[0] * (n + 1) for _ in range(n+1)]

town = 0
answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] != 0:
            cnt = 0
            answer.append(dfs(i, j))
            town += 1


print(town)
answer.sort()
print(*answer, sep='\n')