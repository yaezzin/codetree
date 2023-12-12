a = list(input())
b = list(input())


def is_subsequence(n):
    for i in range(len(b)):
        if a[i + n] != b[i]:
            return False
    
    return True


def is_same():
    for i in range(len(a) - len(b) + 1):
        if is_subsequence(i):
            return i
    
    return -1


print(is_same())