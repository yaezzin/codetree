n, m = map(int, input().split())

time_a = [0] * 1000001
time_b = [0] * 1000001

t1 = 1
for i in range(n):
    v, t = map(int, input().split())
    
    for j in range(t):
        time_a[t1] = time_a[t1-1] + v
        t1 += 1

t2 = 1
for i in range(m):
    v, t = map(int, input().split())
    
    for j in range(t):
        time_b[t2] = time_b[t2-1] + v
        t2 += 1

cnt = 0
for i in range(1, 1000000):
    if time_a[i] > time_b[i] and time_b[i-1] >= time_a[i-1]:
        cnt += 1
    
    elif time_a[i] < time_b[i] and time_b[i-1] <= time_a[i-1]:
        cnt += 1


if cnt != 0:
    print(cnt-1)
else:
    print(0)