# 리스트에 G면 (1)을 또는 H면 (2)를 넣는다 
n, k = map(int, input().split())
lst = [0] * 10001

for _ in range(n):
    location, alphabet = input().split()
    location = int(location)

    if alphabet == 'G':
        lst[location] = 1  
    else:
        lst[location] = 2

answer = 0
for i in range(1, len(lst) - k):
    sum_value = sum(lst[i:i+k+1])
    answer = max(answer, sum_value)

print(answer)