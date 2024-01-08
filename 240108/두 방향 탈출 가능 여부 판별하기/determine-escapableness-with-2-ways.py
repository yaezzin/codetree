def in_range(x, y):
    return x >= 0 and x < n  and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
        
    if visited[x][y] == 1:
        return False
    
    if adj[x][y] == 0:
        return False
    
    return True 

def dfs(x, y):
    # 방문처리 및 더해주기!
    global order
    visited[x][y] = 1
    order += 1
    adj[x][y] = order

    # 아래, 오른쪽 두방향만 이동 가능
    dxs, dys = [1, 0], [0, 1]

    # 방향들을 돌면서 방문 가능한지 확인
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        # 방문 가능하면 dfs 호출하기
        if can_go(new_x, new_y):
            dfs(new_x, new_y)

n, m = map(int, input().split())
visited = [[0] * (n + 1) for _ in range(m + 1)]
adj = []
order = 1
for _ in range(n):
    adj.append(list(map(int, input().split())))


dfs(0,0)

if adj[n-1][m-1] != 0 and adj[n-1][m-1] != 0:
    print(1)
else:
    print(0)