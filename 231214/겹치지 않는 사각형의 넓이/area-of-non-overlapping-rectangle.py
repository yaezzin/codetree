OFFSET = 1000
MAX_R = 2000

seg = [ [0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

# a, b 구하기 
ab = 0
for _ in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            if seg[i][j] == 0:
                seg[i][j] = 1
                ab += 1

cnt = 0         
x1, y1, x2, y2 = tuple(map(int, input().split()))
for i in range(x1, x2):
    for j in range(y1, y2):
        if seg[i][j] == 1:
            cnt += 1

print(ab - cnt)