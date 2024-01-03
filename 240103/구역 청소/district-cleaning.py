lst = [0] * 101

a, b = map(int, input().split())
c, d = map(int, input().split())

for i in range(a, b+1):
    lst[i] = 1

for i in range(c, d+1):
    lst[i] = 1

print(lst.count(1)-1)