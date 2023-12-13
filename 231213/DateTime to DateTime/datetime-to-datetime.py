## 11일 11시 11분 -> a일 b시 c분 까지 몇분?

a, b, c = map(int, input().split())

total = (a * 24 * 60) + (b * 60) + c
total2 = (11 * 24 * 60) + (11 * 60) + 11

print(total - total2)