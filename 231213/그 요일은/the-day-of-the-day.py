days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def func(m, d):
    total = 0
    for i in range(m):
        total += days[i]
    
    total += d

    return total

def func2(input_dow):
    for idx, value in enumerate(dow):
        if value == input_dow:
            return idx


m1, d1, m2, d2 = map(int, input().split())
input_dow = input()

d1 += func2(input_dow)
diff = func(m2, d2) - func(m1, d1)
print(diff // 7 + 1)