n = int(input())
location = [[0] * 2 for _ in range(n+1)]

for _ in range(n):
    num, loc = map(int, input().split())
    location[num][loc] += 1

cnt = 0
for l in location:
    if l[0] != 0 and l[1] != 0:
        cnt += min(l[0], l[1])

print(cnt)