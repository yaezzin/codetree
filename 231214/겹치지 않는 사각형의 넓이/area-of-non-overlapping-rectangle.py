OFFSET = 1000
MAX_R = 2000

seg = [ [0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for n in range(1, 4):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            seg[x][y] = n

cnt = 0
for i in range(0, MAX_R + 1):
    for j in range(0, MAX_R + 1):
        if seg[i][j] == 1 or seg[i][j] == 2:
            cnt += 1

print(cnt)