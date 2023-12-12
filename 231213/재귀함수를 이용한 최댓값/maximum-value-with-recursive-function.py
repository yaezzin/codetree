n = int(input())
lst = list(map(int, input().split()))

m = 0
def func(i):
    global m 

    if i == n:
        return m 

    if lst[i] < m:
        return func(i + 1)
    else:
        m = lst[i]
        return func(i+1)

print(func(0))