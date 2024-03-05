import heapq

n = int(input())
heap = []
for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x)) # 절대값이 가장 작은 수를 출력해야함
    
    else:
        if len(heap) == 0:
            print(0) 
        
        else:
            min_n = heapq.heappop(heap)[1]
            print(min_n)