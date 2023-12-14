MAX_R = 30

n, m = map(int, input().split())
pos_a, pos_b = [0] * (MAX_R + 1), [0] * (MAX_R + 1)


time_a = 1
for _ in range(n):
    d, t = tuple(input().split())
    
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

time_b = 1
for _ in range(m):
    d, t = tuple(input().split())

    for i in range(int(t)):
        pos_b[time_b] = pos_b[time_b -1] + (1 if d == 'R' else - 1)
        time_b += 1

answer = -1
for i in range(1, time_a):
    if pos_a[i] == pos_b[i]:
        answer = i
        break

print(answer)