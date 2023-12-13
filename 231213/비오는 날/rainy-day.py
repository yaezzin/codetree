import sys

n = int(input())

lst = []
for _ in range(n):
    lst.append(tuple(input().split()))

lst.sort(key=lambda x : (x[0]))

m = sys.maxsize
u = ()
for i in range(len(lst)):
    day, date, weather = lst[i]

    if weather == 'Rain':
        tmp = int(''.join(day.split('-')))
        if m > tmp:
            m = tmp
            u = lst[i]


print(*u)