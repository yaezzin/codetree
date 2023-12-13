import math

def func(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0
    for i in range(m):
        total += days[i]
    
    total += d

    return total

def diff_dow(input_dow):
    cnt = 0
    i = 0
    
    while dow[i] != input_dow:
        cnt += 1
        i += 1

    return cnt 
    
dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
input_dow = input()

diff = func(m2, d2) - func(m1, d1)
if diff <= diff_dow(input_dow):
    print(diff // 7)

else:
    print(diff // 7 + 1)