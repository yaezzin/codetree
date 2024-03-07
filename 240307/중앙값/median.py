import heapq

t = int(input())

for _ in range(t):
    m = int(input())
    nums = list(map(int, input().split()))

    max_heap = []
    min_heap = []

    for idx, num in enumerate(nums):
        # 1 ) 힙에 넣어준다.
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
    
        else:
            heapq.heappush(min_heap, num)
        
        # 2 ) 힙의 크기 차이가 2이상이면 더 작은 쪽으로 하나 옮긴다.
        if len(max_heap) > len(min_heap) + 1:
            num = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -num)

        elif len(min_heap) > len(max_heap):
            num = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -num)

        if idx % 2 == 0:
            print(-max_heap[0], end = ' ')
        
    print()