n, k = map(int, map(int, input().split()))
lst = [int(input()) for _ in range(n)]

max_cnt = 0
for i in range(n):
    cnt = 1
    for j in range(i+1, n):
        
        max_value = max(lst[i], lst[j])
        min_value = min(lst[i], lst[j])

        if max_value - min_value <= k:
            cnt += 1
    
    max_cnt = max(cnt, max_cnt)

print(max_cnt)