n, m = map(int, input().split())
lst = [ [0] * n for _ in range(n) ]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for _ in range(m):
    r, c = map(int, input().split())
    
    # 2행 2열로 주어진다면 격자에서는 1행 1열이므로 하나씩 뺴주기
    r = r - 1
    c = c - 1

    # r, c 열이 격자 내에 있으면 색칠 한다.
    if in_range(r, c):
        lst[r][c] = 1

    # 그 이후 상하좌우가 칠해진게 3개 이상인지 확인한다.
    cnt = 0
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]

        if in_range(nx, ny) and lst[nx][ny] == 1:
            cnt += 1

    # 만약 3개 이상이면 1출력 그렇지 않으면 0출력
    if cnt == 3:
        print(1)
    
    else:
        print(0)