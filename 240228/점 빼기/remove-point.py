from sortedcontainers import SortedSet

n, m = map(int, input().split())

ts = SortedSet()

for _ in range(n):
    ts.add(tuple(map(int, input().split())))

for _ in range(n):
    x = int(input())

    idx = ts.bisect_right((x, 0))
    if idx < len(ts):
        print(ts[idx][0], ts[idx][1])
        ts.remove(ts[idx])
    else:
        print(-1, -1)