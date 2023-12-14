n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))


change_point = []
for i in range(len(lst)):
    if i == 0 or lst[i] != lst[i-1]:
        change_point.append(i)

change_point = change_point[::-1]

m = 0
for i in range(1, len(change_point)):
    tmp = change_point[i-1] - change_point[i]
    m = max(tmp, m)

if m == 0:
    print(len(lst))
else:
    print(m)