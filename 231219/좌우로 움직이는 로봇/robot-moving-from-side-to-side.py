OFFSET = 1000001
time_a = [0] * OFFSET
time_b = [0] * OFFSET

n, m = map(int, input().split())

cur_a = 0
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    for i in range(distance):
        time_a[cur_a + 1] = time_a[cur_a] + (1 if direction == 'R' else -1)
        cur_a += 1
    
cur_b = 0
for _ in range(m):
    distance, direction = input().split()
    distance = int(distance)

    for i in range(distance):
        time_b[cur_b + 1] = time_b[cur_b] + (1 if direction == 'R' else -1)
        cur_b += 1


if cur_a > cur_b:
    for i in range(1, cur_a - cur_b + 1):
        time_b[cur_b + i] = time_b[cur_b + i -1]
else:
    for i in range(1, cur_b - cur_a + 1): # 0 1 2 
        time_a[cur_a + i] = time_a[cur_a + i - 1]

cnt = 0
for i in range(1, max(cur_a, cur_b)):
    if time_a[i] == time_b[i]:
        if time_a[i-1] != time_b[i-1]:
            cnt += 1
        

print(cnt)