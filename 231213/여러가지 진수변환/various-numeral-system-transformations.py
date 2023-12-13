n, b = map(int, input().split())

digits = []
while n != 0:
    digits.append(n % b)
    n //= b

print(''.join(map(str, digits[::-1])))