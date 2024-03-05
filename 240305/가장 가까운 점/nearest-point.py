import heapq

n, m = map(int, input().split())

heap = []

for _ in range(n):
    x, y = map(int, input().split())
    distance = abs(x) + abs(y)
    heapq.heappush(heap, (distance, x, y))

for _ in range(m):
    min_num = heapq.heappop(heap)

    # 2씩 더하기
    x, y = min_num[1] + 2, min_num[2] + 2 
    
    # 거리 계산
    distance = abs(x) + abs(y)
    
    # 힙에 넣기
    heapq.heappush(heap, (distance, x, y))


print(heap[0][1], heap[0][2])