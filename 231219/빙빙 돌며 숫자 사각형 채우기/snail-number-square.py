n, m = map(int, input().split())
lst = [[0] * m for _ in range(n)]
lst[0][0] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def solution():
    cur_dir = 0
    x, y = 0, 0
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(2, n * m + 1):
        
        nx = x + dx[cur_dir]
        ny = y + dy[cur_dir]
        
        # 만약 범위를 벗어났거나 0이 아니면 방항 바꾸기
        if not in_range(nx, ny) or lst[nx][ny] != 0:
            cur_dir = (cur_dir + 1) % 4

        x, y = x + dx[cur_dir], y + dy[cur_dir]
        lst[x][y] = i

    for i in range(n):
        for j in range(m):
            print(lst[i][j], end = ' ')
        print()

solution()