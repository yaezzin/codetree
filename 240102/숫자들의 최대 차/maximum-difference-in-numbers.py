MAX_NUM = 10000

n, k = map(int, map(int, input().split()))
lst = [int(input()) for _ in range(n)]

max_cnt = 0

for i in range(1, MAX_NUM + 1):
    # 리스트 안의 숫자가 [최솟값, 최솟값 +k]까지만 가능한 것
    cnt = 0
    for elem in lst:
        if i <= elem and elem <= i + k:
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)