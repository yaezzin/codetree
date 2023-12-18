dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
x, y = 0, 0
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)

    if direction == 'E':
        flag = 0
    elif direction == 'W':
        flag = 1
    elif direction == 'S':
        flag = 2
    elif direction == 'N':
        flag = 3
    
    x += dx[flag] * distance
    y += dy[flag] * distance

print(x, y)