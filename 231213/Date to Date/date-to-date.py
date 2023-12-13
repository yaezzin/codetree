m1, d1, m2, d2 = map(int, input().split())

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 날짜 1에 대해 총 며칠인지 구하기
total1 = 0
for i in range(m1):
    total1 += num_of_days[i]

total1 += d1

# 날짜 2
total2 = 1
for i in range(m2):
    total2 += num_of_days[i]

total2 += d2

print(total2 - total1)