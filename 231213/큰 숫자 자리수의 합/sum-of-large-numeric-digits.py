def func(n):
    if n == 0:
        return 0

    return n % 10 + func(n // 10)
    


a, b, c = map(int, input().split())
d = a * b * c
print(func(d))