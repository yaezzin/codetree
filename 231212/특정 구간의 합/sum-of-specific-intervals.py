n, m = map(int, input().split())
lst_a = list(map(int, input().split()))

for _ in range(m):
    a1, a2 = map(int, input().split())

    s = 0
    for i in range(a1-1, a2):
        s += lst_a[i]
    
    print(s)