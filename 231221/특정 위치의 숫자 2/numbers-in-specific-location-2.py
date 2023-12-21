n = int(input())
lst = list(map(int, input().split()))

s = 0
avg = 0

for i in range(len(lst)):
    if i % 2 != 0:
        s += lst[i]
        avg += 1



print(s, '{:.1f}'.format(s / avg))