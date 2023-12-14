OFFSET = 100
MAX_R = 265

n = int(input())

lst = [ [0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    x, y = x + OFFSET, y + OFFSET

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if lst[i][j] == 0:
                lst[i][j] = 1
                

for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if lst[i][j] == 1:
            cnt += 1

print(cnt)