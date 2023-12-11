def func(a, b):
    if a < b:
        a += 10
        b *= 2
    
    else:
        a *= 2
        b += 10
    
    return a, b

a, b = map(int, input().split())
a, b = func(a, b)
print(a, b)