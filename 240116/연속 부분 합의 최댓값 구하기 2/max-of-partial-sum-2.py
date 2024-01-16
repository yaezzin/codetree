n = int(input())
lst = list(map(int, input().split()))

s = 0
answer = 0
for i in range(len(lst)):
    if s < 0:
        s = 0

    s += lst[i]
    answer = max(answer, s)


if s < 0:
    print(-1)
else:
    print(answer)