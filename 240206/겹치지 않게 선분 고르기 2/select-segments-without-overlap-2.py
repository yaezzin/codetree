n = int(input())
times = []

for _ in range(n):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x : x[1])

cnt = 1
pivot = times[0]
for i in range(1, n):
    if pivot[1] < times[i][0]:
        pivot = times[i]
        cnt += 1
    
print(cnt)