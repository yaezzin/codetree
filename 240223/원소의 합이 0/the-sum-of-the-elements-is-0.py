from collections import defaultdict

n = int(input())

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
a4 = list(map(int, input().split()))

d1 = defaultdict(lambda: 0)
d2 = defaultdict(lambda: 0)

ans = 0
for i in range(n):
    for j in range(n):
        d1[a1[i] + a2[j]] += 1

for i in range(n):
    for j in range(n):
        d2[a3[i] + a4[j]] += 1

answer = 0
for k1 in d1.keys():
    diff = 0 - k1

    if diff in d2: 
        answer += d1[k1] * d2[diff]

print(answer)