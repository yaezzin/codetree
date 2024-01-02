n, k = map(int, input().split())
lst = [int(input()) for i in range(n)]

bomb = {}
for i in range(n):
    for j in range(i+1, n):
        if lst[i] == lst[j] and j - i <= k:
            if lst[i] in bomb:
                bomb[lst[i]] += 1
            else:
                bomb[lst[i]] = 1

max_value = (0, 0)
for idx, value in bomb.items():
    if max_value[1] <= value:
        max_value = (idx, value)

print(max_value[0])