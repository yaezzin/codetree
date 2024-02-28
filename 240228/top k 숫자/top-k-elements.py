from sortedcontainers import SortedSet

n, m = map(int, input().split())
ts = SortedSet(map(int, input().split()))

for i in range(1, m + 1):
    print(ts[-1 * i], end = ' ')