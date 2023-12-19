v = list(input())

x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

cur = 3 # 기본값은 북쪽
t = 0
answer = -1
for s in v:
    if s == 'F':
        x = x + dx[cur]
        y = y + dy[cur]

    elif s == 'L':
        cur = (cur - 1 + 4) % 4
    
    elif s == 'R':
        cur = (cur + 1) % 4
    
    t += 1
    
    if x == 0 and y == 0:
        answer = t
        break

print(answer)