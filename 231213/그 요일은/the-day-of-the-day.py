import math

# 며칠 차이가 나는지 확인하기
def func(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0
    for i in range(m):
        total += days[i]
    
    total += d

    return total

# 월요일과 x요일이 얼마나 차이나는지 확인
def func2(input_dow):
    dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    cnt = 0
    i = 0    
    
    while dow[i] != input_dow:
        cnt += 1
        i += 1

    return cnt 
    

m1, d1, m2, d2 = map(int, input().split())
input_dow = input()

diff = func(m2, d2) - func(m1, d1)
diff_dow = func2(input_dow)

if diff // 7 > diff_dow:
    print((diff - diff_dow) // 7 + 1)
else:
    print((diff - diff_dow) // 7)