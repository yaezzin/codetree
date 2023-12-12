def f(n):
    if n <= 0:
        return 0
    return n + f(n-2)
    

n = int(input())
print(f(n))