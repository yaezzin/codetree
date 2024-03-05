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
        three_nums = nsmallest(3, heap)        
        
        answer = 1
        for t in three_nums:
            answer *= t
        
        print(answer)