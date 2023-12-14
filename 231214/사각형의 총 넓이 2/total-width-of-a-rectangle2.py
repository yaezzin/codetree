OFFSET = 100
MAX_R = 200
n = int(input())

lst = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

cnt = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET


    for i in range(x1, x2):
        for j in range(y1, y2):
            if lst[i][j] == 0:
                lst[i][j] = 1
                cnt += 1

print(cnt)