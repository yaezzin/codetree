OFFSET = 10000

n = int(input())

lst = []
for i in range(n):
    s, e = map(int, input().split())
    s += OFFSET
    e += OFFSET
    lst.append([s, e])

ms = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i == j or j == k or i ==k:
                continue
            
            x1, y1 = lst[i][0], lst[i][1]
            x2, y2 = lst[j][0], lst[j][1]
            x3, y3 = lst[k][0], lst[k][1]

            if (x1 == x2 or x2 == x3 or x1 == x3) and (y1 == y2 or y2 == y3 or y3 == y1):
                s1 = x1 * y2 + x2 * y3 + x3 * y1
                s2 = x2 * y1 + x3 * y2 + x1 * y3
                s = abs(s1 -s2)
                ms = max(ms, s)

print(ms)