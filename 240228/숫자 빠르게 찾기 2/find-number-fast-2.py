from sortedcontainers import SortedSet

n, m = map(int, input().split())
ts = SortedSet(map(int, input().split()))

for _ in range(m):
    k = int(input())

    idx = ts.bisect_left(k)
    if idx < len(ts):
        print(ts[idx])
    else:
        print(-1)