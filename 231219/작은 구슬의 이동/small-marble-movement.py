direction = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 입력 
n, t = map(int, input().split())
r, c, d = input().split()

# 변환
r, c = int(r), int(c)
idx = direction[d]

for _ in range(t):
    # r행 c열에서 d 방향으로 t초 동안 이동했을 때의 위치
    nx = r + dx[idx]
    ny = c + dy[idx]
    
    # 만약 범위 안에 있으면
    if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
        r = nx
        c = ny
    
    # 만약 범위를 벗어나면 방향 반대로 바꿔주기
    else:
        idx = 3 - idx

print(r, c)