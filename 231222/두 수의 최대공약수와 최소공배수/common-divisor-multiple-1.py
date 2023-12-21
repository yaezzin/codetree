def lcm(x,y):
    return x * y // gcd(x, y)  

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    
    return x

a, b = map(int, input().split())
print(gcd(a,b), lcm(a, b))