from collections import Counter

n, k = map(int, input().split())
nums = list(map(int, input().split()))

dic = {}
for n in nums:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

answer = []
max_n = max(dic.values())
for k, v in dic.items():
    if v == max_n:
        answer.append(k)

answer.sort(reverse=True)
print(*answer, end = ' ')