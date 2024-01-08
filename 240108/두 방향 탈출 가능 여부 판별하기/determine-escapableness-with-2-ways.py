def in_range(x, y):
    return x >= 0 and x < n  and y >= 0 and y < n

def dfs(x, y):
    # 방문처리
    visited[x][y] = 1
    adj[x][y] += 1 

    # 아래, 오른쪽 두방향만 이동 가능
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        # 방문을 안했고, 범위 안에 있고, 뱀이 없다면 -> dfs 호출하기
        if in_range(new_x, new_y) and not visited[new_x][new_y] and adj[new_x][new_y] != 0:
            dfs(new_x, new_y)

n, m = map(int, input().split())
visited = [[0] * (n + 1) for _ in range(n+1)]
adj = []
for _ in range(n):
    adj.append(list(map(int, input().split())))

dfs(0,0)

if adj[n-1][n-1] == 2:
    print(1)
else:
    print(0)