n, t = map(int, input().split())
command = list(input())
lst = [ list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def solution():
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