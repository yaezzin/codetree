n = int(input())
lst = list(map(int, input().split()))

def func(i):
    if i == n:
        return lst[0]

    return max(func(i+1), lst[i])

print(func(0))