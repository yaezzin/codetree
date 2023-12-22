import sys

n, h, t = map(int, input().split())
lst = list(map(int, input().split()))

# 구간이 t번 이상 높이가 h로 나와야 하는 최소비용 
min_value = sys.maxsize

for i in range(n-t+1):
    tmp = lst[i:i+t]   

    cnt = 0
    for i in range(len(tmp)):
        while tmp[i] != h:
            if tmp[i] > h:
                tmp[i] -= 1
            else:
                tmp[i] += 1
            cnt += 1
    
    min_value = min(min_value, cnt)

print(min_value)