def onjeon(a, b):
    cnt = 0
    for n in range(a, b+1):
        if n % 2 != 0 and n % 10 != 5 and (n % 3 != 0 or n % 9 == 0):
            cnt += 1
    return cnt 

a, b = map(int, input().split())
print(onjeon(a, b))