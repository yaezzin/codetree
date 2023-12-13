def decimal(k, a):
    lst = [int(digit) for digit in str(k)]

    m = 0
    for i in range(len(lst)):
        m = m * a + lst[i]
    
    return m

def binary(k, b):
    binary_lst = []
    while k != 0:
        binary_lst.append(k % b)
        k //= b

    return binary_lst[::-1]

# 8진수로 표현된걸 10진수로 변환
a, b = map(int, input().split())
n = int(input())

tmp = decimal(n, a)
result = binary(tmp, b) 

print(''.join(map(str, result)))