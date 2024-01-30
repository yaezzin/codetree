n = int(input())
x, y = map(int, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

cur_dir = 0
answer = 0

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def simulate(x, y): 
    global cur_dir
    global answer
    
    while True:
        nx, ny = x + dx[cur_dir], y + dy[cur_dir]

        if in_range(nx, ny) and not visited[nx][ny]:
            # 1 ) 바라보고 있는 방향으로 이동 불가능한 경우 반시계 방향 회전
            if grid[nx][ny] == '#': 
                cur_dir = (cur_dir -1 + 4) % 4
        
            # 2 ) 벽이 있는 경우
            elif grid[nx][ny] == '.':
                tmp_dir = (cur_dir + 1) % 4
                tmp_x = nx + dx[tmp_dir]
                tmp_y = ny + dy[tmp_dir]
                
                # 오른쪽에 벽이 있다면 한칸 이동
                if in_range(tmp_x, tmp_y) and grid[tmp_x][tmp_y] == '#':
                    x, y = nx, ny
                    visited[x][y] = 1
                    answer += 1
            
                # 없다면 한칸 이동 후 시계방향 회전하여 한칸 더 이동
                else:
                    x, y = nx, ny
                    visited[x][y] = 1

                    cur_dir = (cur_dir + 1) % 4
                    x, y = x + dx[cur_dir], y + dy[cur_dir]
                    visited[x][y] = 1

                    answer += 2

        # 이동 가능하나 사이클이 존재하면 -1  
        elif in_range(nx, ny) and visited[nx][ny]:
            answer = -1
            break

        # 2 ) 바라보는 방향으로 이동이 불가능하면 탈출
        else:
            answer += 1
            break

    print(answer)
       

simulate(x-1, y-1)