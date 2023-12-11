def is_3_multiples(n):
    return n % 3 == 0
    
def is_369(n):
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        else:
            n //= 10
    
    return False

a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    if is_3_multiples(i) or is_369(i):
        cnt += 1

print(cnt)