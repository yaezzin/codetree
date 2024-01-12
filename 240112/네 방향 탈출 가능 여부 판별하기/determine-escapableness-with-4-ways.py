from collections import deque

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and graph[x][y]

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):

            new_x = x + dx
            new_y = y + dy

            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = 1
   
                
        
n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
q = deque()

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

q.append((0, 0))
visited[0][0] = 1
bfs()

answer = 1 if visited[n-1][m-1] == 1 else 0
print(answer)