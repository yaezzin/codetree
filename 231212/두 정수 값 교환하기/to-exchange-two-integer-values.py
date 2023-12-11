# 불변 -> 복사해서 넘김 
def swap(n, m):
    n, m = m, n
    print(n, m)

a, b = map(int, input().split())
swap(a, b)