n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1

grid = [list(input()) for _ in range(n)]
visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]

cur_dir = 0
answer = 0

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def simulate(): 
    global x, y, cur_dir
    global answer
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    while in_range(x, y):
        
        # 1 ) 이미 방문했으면 탈출 불가능하며, 방문 안했으면 방문처리 해주기
        if visited[x][y][cur_dir]:
            answer = -1 
            break
        
        else:
            visited[x][y][cur_dir] = True


        # 2 ) 탈출 가능한지 조사하기
        nx, ny = x + dx[cur_dir], y + dy[cur_dir]

        if in_range(nx, ny) and grid[nx][ny] == '#':
            cur_dir = (cur_dir -1 + 4) % 4
        
        elif not in_range(nx, ny):
            answer += 1
            break
        
        elif in_range(nx, ny) and grid[nx][ny] == '.':
            tmp_dir = (cur_dir + 1) % 4
            tmp_x = nx + dx[tmp_dir]
            tmp_y = ny + dy[tmp_dir]
            
            # 오른쪽에 벽이 있다면 한칸 이동
            if in_range(tmp_x, tmp_y) and grid[tmp_x][tmp_y] == '#':
                x, y = nx, ny
                answer += 1
        
            # 없다면 한칸 이동 후 시계방향 회전하여 한칸 더 이동
            else:
                x, y = tmp_x, tmp_y
                cur_dir = (cur_dir + 1) % 4
                answer += 2


    print(answer)
       

simulate()