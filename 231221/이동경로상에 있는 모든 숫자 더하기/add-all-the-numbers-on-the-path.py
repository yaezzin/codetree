n, t = map(int, input().split())
command = list(input())
lst = [[0] * n for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def fill_lst(n):
    k = 1
    for i in range(n):
        for j in range(n):
            lst[i][j] = k
            k += 1
    
def solution():
    fill_lst(n)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    
    cur_dir = 3 # 현재 북쪽 
    x, y = n // 2, n // 2
    s = lst[x][y]

    for i in range(t):
        c = command[i]

        if c == 'L':
            cur_dir = (cur_dir -1 + 4) % 4 

        elif c == 'R':
            cur_dir = (cur_dir + 1) % 4

        elif c == 'F':
            nx = x + dx[cur_dir]
            ny = y + dy[cur_dir]

            if in_range(nx, ny):
                x = x + dx[cur_dir]
                y = y + dy[cur_dir]
                
                s += lst[x][y]

    print(s)
    
solution()