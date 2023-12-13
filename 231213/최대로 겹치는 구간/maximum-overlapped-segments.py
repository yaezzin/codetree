n = int(input())

lst = [0 for _ in range(100)]

for _ in range(n):
    s, e = map(int, input().split())

    for i in range(s, e):
        lst[i] += 1
    
print(lst.count(max(lst)) - 1)