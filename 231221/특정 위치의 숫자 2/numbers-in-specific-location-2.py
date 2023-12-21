n = int(input())
lst = list(map(int, input().split()))

s = 0
for i in range(len(lst)):
    if i % 2 != 0:
        s += lst[i]

print(s, s / (n // 2))