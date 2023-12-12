def func(n):
    if n == 1:
        return 2
    
    if n == 2:
        return 4
    
    return func(n-1) * func(n-2) % 100

n = int(input())
print(func(n))