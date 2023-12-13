# m1 d1이 월요일이면 m2 d2은 무슨 요일인가?
# 흐른 날짜를 계산한다. 
def func(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0
    for i in range(1, m):
        total += days[i]
    
    total += d
   
    return total


# 메인
m1, d1, m2, d2 = map(int, input().split())
tmp1 = func(m1, d1)
tmp2 = func(m2, d2)

diff = tmp2 - tmp1
diff %= 7

dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(dow[diff])