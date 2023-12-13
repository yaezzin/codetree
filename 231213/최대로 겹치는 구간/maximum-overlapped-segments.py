n = int(input())

lst = [0 for _ in range(201)]

for _ in range(n):
    s, e = map(int, input().split())
    
    s += 100
    e += 100

    for i in range(s, e):
        lst[i] += 1

print(max(lst))