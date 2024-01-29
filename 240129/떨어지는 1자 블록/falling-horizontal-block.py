# k번쨰 열부터 k + m - 1째 열까지 공간을 차지함
# 아래로 내려갈 수 있을때까지 반복 (다른 블럭과 맞닿거나 바닥에 떨어지면 종료)

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n 

def simulate(x, y):    
    dx, dy = 0, 1

    for i in range(y, y + m):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 0:
            x, y = nx, ny
        
        else:
            return False
    
    return True

max_row = -1
for i in range(n): 
    # k-2로 주는 이유는 자기자신부터 검증하기 위해 (위에서 처음부터 한칸씩 이동시키기 때문에)
    can_go = simulate(i, k-2) 
   
    if can_go:
        max_row = i
    
    else:
        break

for i in range(k-1, k+m-1):
    grid[max_row][i] = 1

for g in grid:
    print(*g)