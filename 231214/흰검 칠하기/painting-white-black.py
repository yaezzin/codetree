OFFSET = 100000
MAX_R = 200000


n = int(input())

segments = []
cur = 0
color = ''
for _ in range(n):
    
    distance, direction = tuple(input().split())
    distance = int(distance)
    
    if direction == 'L':
        left = cur - distance + 1
        right = cur
        cur = cur - distance + 1
        color = 'W'

    else:
        left = cur
        right = cur + distance - 1
        cur = cur + distance - 1
        color = 'B'
        
    segments.append([left, right, color])

# [흰색][검정][현재 색깔 0, 1]
checked = [ [0] * 3 for _ in range(MAX_R + 1)] 
for x1, x2, c in segments:
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    color = c

    if color == 'B':
        for i in range(x1, x2 + 1):
            checked[i][1] += 1
            checked[i][2] = 1

    else:
        for i in range(x1, x2 + 1):
            checked[i][0] += 1
            checked[i][2] = 0

       
gray = 0
black = 0
white = 0
for i in range(len(checked)):
    if checked[i][0] >= 2 and checked[i][1] >= 2:
        gray += 1

    elif checked[i][0] == 1 and checked[i][2] == 1:
        black += 1

    elif checked[i][0] == 1 and checked[i][2] == 0:
        white += 1

print(white, black, gray)