from heapq import nsmallest
import heapq

n = int(input())
nums = list(map(int, input().split()))

heap = []
for num in nums: 
    heapq.heappush(heap, num)

    if len(heap) < 3:
        print(-1)
    else:
        num1 = heapq.heappop(heap)    
        num3 = heapq.heappop(heap)    
        num2 =heapq.heappop(heap)    
        
        print(num1 * num2 * num3)

        heapq.heappush(heap, num1)
        heapq.heappush(heap, num2)
        heapq.heappush(heap, num3)