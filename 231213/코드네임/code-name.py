import sys

user = [tuple(input().split()) for _ in range(5)]

m = sys.maxsize
answer = ()
for u in user:
    if int(u[1]) < m:
        m = int(u[1])
        answer = u

print(*answer)