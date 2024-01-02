import sys

# a = 4라는 것은 답의 최대가 4라는 것
n, k = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
for a in range(1, max(lst) + 1):
    
    tmp = []
    for idx, elem in enumerate(lst):
        if elem <= a:
            tmp.append(idx)
    
    flag = 1
    for i in range(1, len(tmp)):
        distance = tmp[i] - tmp[i-1]
        
        if distance > k:
            flag = 0
    
    if flag == 1:
        answer = max(answer, a)

print(answer)