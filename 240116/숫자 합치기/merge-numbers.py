from collections import deque

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

q = deque(lst)

s = 0
while len(q) > 1:
    first = q.popleft()
    second = q.popleft()
    q.append(first + second)
    s += first + second
    q = deque(sorted(q))

print(s)