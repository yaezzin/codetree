from sortedcontainers import SortedSet

n, m = map(int, input().split())
ts = list(map(int, input().split()))

balls = SortedSet([i for i in range(1, m + 1)])

for elem in ts:
    balls.remove(elem)
    print(balls[-1])