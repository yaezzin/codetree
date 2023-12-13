import sys

users = [ ]
for _ in range(5):
    name, score = tuple(input().split())
    users.append((name, int(score)))

m = sys.maxsize

answer = ()
for user in users:
    name, score = user

    if score < m:
        m = score
        answer = user

print(*answer)