def decimal(lst):
    m = 0

    for i in range(len(lst)):
        m = m * 2 + lst[i]
    
    return m

def binary(n):
    lst = []

    while n != 0:
        lst.append(n%2)
        n //= 2
    
    return lst[::-1]

# 입력
n = list(map(int, list(input())))

# 10진수로 바꾼다
d = decimal(n)

# 17배
d *= 17

# 2진수로 바꾼다
result = ''.join(map(str, binary(d)))
print(result)