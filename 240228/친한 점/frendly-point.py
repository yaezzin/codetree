from sortedcontainers import SortedSet

n, m = map(int, input().split())

ts = SortedSet()
for _ in range(n):
    ts.add(tuple(map(int, input().split())))

for _ in range(m):
    a, b = map(int, input().split())

    idx = ts.bisect_left((a, b))
    if idx < len(ts):
        print(ts[idx][0], ts[idx][1])
    else:
        print(-1, -1)