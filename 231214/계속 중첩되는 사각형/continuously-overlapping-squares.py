OFFSET = 100
MAX_R = 200

n = int(input())

checked = [ [0] * (MAX_R + 1) for _ in range(MAX_R + 1)]
for idx in range(n):
    x1, y1, x2, y2 = map(int, input().split())  

    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            if idx % 2 == 0:
                checked[x][y] = 0 # 짝수면 빨간색 0
            else: 
                checked[x][y] = 1 # 홀수면 파란색 1

cnt = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if checked[i][j] == 1:
            cnt += 1

print(cnt)