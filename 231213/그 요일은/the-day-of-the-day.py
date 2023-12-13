m1, d1, m2, d2 = map(int, input().split())

def func(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0
    for i in range(m):
        total += days[i]
    
    total += d

    return total

diff = func(m2, d2) - func(m1, d1)
print(diff % 7)