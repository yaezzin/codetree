import heapq


n = int(input())
nums = list(map(int, input().split()))
heap = [-num for num in nums]  # 최대값을 위해 -를 붙여주기
heapq.heapify(heap)

while len(heap) >= 2:
    max_num1 = -heapq.heappop(heap)
    max_num2 = -heapq.heappop(heap)
    diff = max_num1 - max_num2

    if diff != 0:
        heapq.heappush(heap, -diff)

if len(heap) == 0:
    print(-1)
else:
    print(-heap[0])