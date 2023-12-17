import sys

INT_MIN = sys.maxsize

n = int(input())
lst = list(map(int, input().split()))

answer = INT_MIN
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += lst[j] * abs(j - i)

    answer = min(answer, tmp)

print(answer)