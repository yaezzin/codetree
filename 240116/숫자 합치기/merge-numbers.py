import heapq

n = int(input())
lst = list(map(int, input().split()))
heapq.heapify(lst)

answer = 0
while len(lst) > 1:
    f = heapq.heappop(lst)
    s = heapq.heappop(lst)

    answer += (f + s)

    heapq.heappush(lst, f + s)

print(answer)