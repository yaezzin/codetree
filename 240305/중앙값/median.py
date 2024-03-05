import heapq

t = int(input())

for _ in range(t):
    
    m = int(input())
    nums = list(map(int, input().split()))

    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])

        if i % 2 == 0: # 홀수라면 중앙값 출력
            
            print(nums[len(heap) // 2],end = ' ')
    
    print()