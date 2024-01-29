def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def simulate(x, y):
    # 상하좌우 순서대로 우선순위 가짐 (우좌하상 순으로 정의하기)
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    answer = [grid[x][y], ]

    while True:
        max_pos = (-1, -1)
        max_num = grid[x][y]
        max_dir = -1

        for idx, (dx, dy) in enumerate(zip(dxs, dys)):
            nx, ny = x + dx, y + dy

            # 범위 안에 있고, 숫자가 더 크다면
            if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
                
                # 우선순위가 더 높다면 변경
                if idx > max_dir:
                    max_num = grid[nx][ny]
                    max_pos= (nx, ny)
                    max_dir = idx
        
    
        # 만약에 
        if max_num == grid[x][y]:
            break 
        
        else:
            x, y = max_pos
            answer.append(max_num)

        
    return answer

n, r, c = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(n)]
print(*simulate(r-1, c-1))