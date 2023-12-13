h1, m1, h2, m2 = map(int, input().split())

# 2시 5분 ~ 4시 1분까지의 시간
total1 = h1 * 60 + m1
total2 = h2 * 60 + m2 
print(total2 - total1)