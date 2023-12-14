OFFSET == 100
#

n = int(input())

lst = [ [0] * 165 for _ in range(165)]

cnt = 0
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if lst[i][j] == 0:
                lst[i][j] = 1
                

for i in range(165):
    for j in range(165):
        if lst[i][j] == 1:
            cnt += 1

print(cnt)