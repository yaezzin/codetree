import sys

n, k = map(int, input().split())
lst = list(map(int, input().split()))

answer = sys.maxsize
for i in range(1, 10001):
    tmp = 0 
    for j in range(len(lst)):
        if lst[j] >= i and lst[j] <= i + k:
            continue
        else:
            tmp += min(abs(lst[j]-i), abs(lst[j]-i-k))
    
    answer = min(answer, tmp)

print(answer)