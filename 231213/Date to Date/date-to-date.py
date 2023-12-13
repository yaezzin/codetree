m1, d1, m2, d2 = map(int, input().split())

def num_of_days(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0
    for i in range(1, m):
        total += days[i]

    total += d

    return total

result = num_of_days(m2, d2) - num_of_days(m1, d1) + 1
print(result)