# 1. 한명을 해고했을 떄 운행되고 있는 시간이 최대가 되도록 해라
n = int(input())

# 2. 입력받기 
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append([s, e])

# 3. 답 구하기
max_value = 0
for i in range(n):
    time = [0] * 1000

    for j in range(n):
        if i == j:
            continue

        start, end = lst[j]
        
        for k in range(start, end):
            time[k] = 1

    max_value = max(max_value, time.count(1))


print(max_value)