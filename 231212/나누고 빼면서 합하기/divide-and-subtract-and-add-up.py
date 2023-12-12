n, m = map(int, input().split())
lst = list(map(int, input().split()))


s = 0
while m >= 1:
    
    s += lst[m-1]

    if m % 2 == 0:
        m //= 2
    
    else:
        m -= 1

print(s)