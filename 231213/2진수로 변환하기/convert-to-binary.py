n = int(input())

digits = []
while n != 0:
    if n % 2 == 0:
        digits.append(0)
    else:
        digits.append(1)

    n //= 2

print(''.join(map(str, digits[::-1])))