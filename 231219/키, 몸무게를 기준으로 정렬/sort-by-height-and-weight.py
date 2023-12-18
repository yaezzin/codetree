n = int(input())
lst = [input().split() for _ in range(n)]
lst.sort(key=lambda x : (x[1], -(int(x[2]))))
for l in lst:
    n, h, w = l
    print(n, h, w)