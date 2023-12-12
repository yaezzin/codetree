import sys

user = [tuple(input().split()) for _ in range(5)]

m = sys.maxsize
answer = ()
for u in user:
    name, score = u

    if int(score) < m:
        m = int(score)
        answer = u

print(*answer)