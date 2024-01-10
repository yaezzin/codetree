def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def can_go(x, y):
    # 범위에 없거나, 이미 방문했거나, 
    if not in_range(x, y) or visited[x][y] == 1:
        return False
    
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
            if grid[new_x][new_y] == grid[x][y]:
                dfs(new_x, new_y)


n = int(input())

visited = [[0] * (n + 1) for _ in range(n+1)]
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

answer = []
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

count = [i for i in answer if i >= 4]
max_value = max(answer)
print(len(count), max_value)