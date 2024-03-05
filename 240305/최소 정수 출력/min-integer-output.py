import heapq

n = int(input())
heap = []

for _ in range(n):
    m = int(input())

    # 입력이 자연수이면 힙에 넣기
    if m > 0:
        heapq.heappush(heap, m)
    
    # 입력이 0 이라면 가장 작은값 출력하고 제거
    elif m == 0:
        if len(heap) == 0:
            print(0)
        else:
            min_num = heapq.heappop(heap)
            print(min_num)