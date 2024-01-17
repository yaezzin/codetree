n = int(input())

time = []
for _ in range(n):
    s, e = map(int, input().split())
    time.append([s, e])


time.sort(key= lambda x: (x[1], x[0]))
pivot = time[0][1]

answer = 1
for i in range(1, len(time)):
    if pivot <= time[i][0]:
        answer += 1 
        pivot = time[i][1]

print(n - answer)