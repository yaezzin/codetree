n, b = map(int, input().split())

digits = []
while n != 0:
    digits.append(n%4)
    n //= 4

print(''.join(map(str, digits[::-1])))