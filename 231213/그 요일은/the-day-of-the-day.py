def func(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0
    for i in range(m):
        total += days[i]
    
    total += d

    return total

m1, d1, m2, d2 = map(int, input().split())
input_dow = input()

dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
if d1 != d2:
    i = 0
    while dow[i] != input_dow:
        d1 += 1
        i += 1 

diff = func(m2, d2) - func(m1, d1)
print(diff // 7 + 1)