def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_even(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    
    if s % 2 == 0:
        return True
    
    return False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_even(i):
        cnt += 1
print(cnt)