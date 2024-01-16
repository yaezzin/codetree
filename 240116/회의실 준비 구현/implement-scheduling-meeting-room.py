n = int(input())

time = []
for _ in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

time.sort(lambda x : (x[1], x[0]))

answer = 1
check = time[0][1]
for i in range(1, n):
    if check <= time[i][0]:
        answer += 1  
        check = time[i][1]

print(answer)