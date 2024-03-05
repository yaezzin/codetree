import heapq

n = int(input())
heap = []

for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation.startswith("push"):
        num = int(command[1])
        heapq.heappush(heap, (-num, num))

    elif operation.startswith("pop"):
        num = heapq.heappop(heap)
        print(num[1])

    elif operation.startswith("size"):
        print(len(heap))
    
    elif operation.startswith("empty"):
        if heap:
            print(0)
        else:
            print(1)

    elif operation.startswith("top"):
        max_num = heap[0][1]
        print(max_num)