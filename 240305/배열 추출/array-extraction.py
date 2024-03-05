import heapq

n = int(input())

heap = []
for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, (-x, x))

    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            max_num = heapq.heappop(heap)
            print(max_num[1])