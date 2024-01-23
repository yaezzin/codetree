n, t = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
#c = c[::-1]

for _ in range(t):
    # 마지막 저장
    tmp1, tmp2, tmp3 = a[n-1], b[n-1], c[n-1]


    for i in range(n - 1, 0, -1):
        a[i] = a[i-1]
    
    a[0] = tmp3

    for i in range(n-1, 0, -1):
        b[i] = b[i-1]
    
    b[0] = tmp1

    for i in range(n-1, 0, -1):
        c[i] = c[i-1]
    
    c[0] = tmp2

print(*a)
print(*b)
print(*c)