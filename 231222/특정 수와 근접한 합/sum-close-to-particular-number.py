import sys

n, s = map(int, input().split())
lst = list(map(int, input().split()))

total_sum = sum(lst)
min_value = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        tmp = lst[i] + lst[j]
        min_value = min(min_value, abs(s - (total_sum - tmp)))
    
print(min_value)