OFFSET = 100000
MAX_R = 200000

n = int(input())

cur = 0
segments = []
for _ in range(n):  
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'R':
        left = cur
        right = cur + distance - 1
        cur = cur + distance - 1
        color = 1

    else:
        left = cur - distance + 1
        right = cur
        cur = cur - distance + 1
        color = 0
        
    segments.append([left, right, color])

checked = [9] * (MAX_R + 1)
for x1, x2, color in segments:
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    if color == 0:
        for i in range(x1, x2 + 1):
            checked[i] = 0
    
    else:
        for i in range(x1, x2 + 1):
              checked[i] = 1


black = 0
white = 0
for c in checked:
    if c == 0:
        white += 1
    
    elif c == 1:
        black += 1

print(white, black)