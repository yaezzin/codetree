n = int(input())

lst = [ 0 for _ in range(101) ]

for _ in range(n):
    s, e = map(int, input().split())

    for i in range(s, e + 1):
        lst[i] += 1

print(max(lst))