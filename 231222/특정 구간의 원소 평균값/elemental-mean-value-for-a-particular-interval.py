# i j k
# 0 0 0 1 # 첫번쨰 요소 한칸만
# 0 1 0 2 # 첫번쨰 요소랑 그 다음칸
# 0 2 0 3 

n = int(input())
lst = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        s = 0
        for k in range(i, j+1):
            s += lst[k]
        
        avg = s / (abs(j - i) + 1)
        if avg in lst[i:j+1]:
            cnt += 1

print(cnt)