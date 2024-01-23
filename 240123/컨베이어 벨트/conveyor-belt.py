n, t = map(int, input().split())
grid = [ list(map(int, input().split())) for _ in range(2)]

grid[1] = grid[1][::-1]

for _ in range(t):
    # 윗줄의 맨 오른쪽 담아둔다.
    tmp1 = grid[0][n-1]

    # 밑줄의 맨 왼쪽을 담아둔다.
    tmp2 = grid[1][0]

    # 윗줄 오른쪽으로 밀당하기
    for i in range(n-1, -1, -1):
        grid[0][i] = grid[0][i-1]

    grid[0][0] = tmp2

    # 아랫줄 왼쪽으로 밀당하기
    for i in range(n-1):
        grid[1][i] = grid[1][i+1]

    grid[1][n-1] = tmp1


grid[1] = grid[1][::-1]

for g in grid:
    print(*g)