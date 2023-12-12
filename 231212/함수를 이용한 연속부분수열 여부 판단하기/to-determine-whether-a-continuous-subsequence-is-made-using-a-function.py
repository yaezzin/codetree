# 연속 부분 수열인지 체크하기

def is_same(n):
    for i in range(n2):
        if a[n + i] != b[i]: # 여기가 체크하는 부분
            return False

    return True

def is_subsequence():
    for i in range(n1 - n2 + 1):
        if is_same(i):
            return True

    return False

n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if is_subsequence():
    print('Yes')
else:
    print('No')