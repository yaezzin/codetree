a, b = map(int, input().split())
n = int(input())

def decimal(k):
    lst = [int(digit) for digit in str(k)]

    m = 0
    for i in range(len(lst)):
        m = m * 8 + lst[i]
    
    return m

def binary(k):
    binary_lst = []
    while k != 0:
        binary_lst.append(k % 2)
        k //= 2

    return binary_lst[::-1]

# 8진수로 표현된걸 10진수로 변환
tmp = decimal(n)
result = binary(tmp) 

print(''.join(map(str, result)))