def s(n):
    if n == 0:
        return 0
    
    return (n % 10) ** 2 + s(n // 10)


n = int(input())
print(s(n))