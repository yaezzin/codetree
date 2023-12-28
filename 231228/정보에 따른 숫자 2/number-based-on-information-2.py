import sys

T, a, b = map(int, input().split())

lst = []
for i in range(T):
    c, x = input().split()
    lst.append([c, int(x)])

# a ~ b까지의 K를 탐색


cnt = 0
for k in range(a, b+1):
    d1, d2 = 1000, 1000 
    
    for l in lst:
        c = l[0]
        x = l[1]

        if c == 'S':
            d1 = min(d1, abs(k - x))

        else:
            d2 = min(d2, abs(k - x))

    if d1 <= d2:
        cnt += 1
            
print(cnt)