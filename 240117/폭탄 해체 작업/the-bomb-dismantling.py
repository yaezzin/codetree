n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x : (x[1], -x[0]))
answer = 0
pivot = lst[0][1]

answer += lst[0][0]
for i in range(1, len(lst)):
    if pivot < lst[i][1]:
        answer += lst[i][0]
        pivot = lst[i][1]

print(answer)