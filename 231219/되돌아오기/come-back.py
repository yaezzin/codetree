n = int(input())

d = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
t = 0
answer = -1

lst = []
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    lst.append([direction, distance])

flag = 0
for i in range(n):
    direction, distance = lst[i]
    cur = d[direction]
    
    for _ in range(distance):
        x = x + dx[cur]
        y = y + dy[cur]
        
        t += 1

        if x == 0 and y == 0:
            answer = t
            flag = 1
    
    if flag == 1:
        break

print(answer)