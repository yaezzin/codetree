MAX_R = 1000001

n, m = map(int, input().split())

time_a, time_b = [0] * MAX_R, [0] * MAX_R
cur_a, cur_b = 1, 1

for _ in range(n):
    v, t = map(int, input().split())
    
    for _ in range(t):
        time_a[cur_a] = time_a[cur_a-1] + v
        cur_a += 1
     
for _ in range(m):
    v, t = map(int, input().split())
    
    for _ in range(t):
        time_b[cur_b] = time_b[cur_b-1] + v
        cur_b += 1

#               o     o   o  o
# a : [0, 1, 2, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27 ]
# b : [0, 2, 4, 6, 7, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35 ]
cnt = 0
for i in range(1, max(cur_a, cur_b)):
    if time_b[i] > time_a[i]:
        if time_a[i-1] >= time_b[i-1]:
            cnt += 1
            
    
    elif time_a[i] > time_b[i]:
        if time_b[i-1] >= time_a[i-1]:
            cnt += 1
    
    else:
        if time_a[i-1] != time_b[i-1]:
            cnt += 1

print(cnt)