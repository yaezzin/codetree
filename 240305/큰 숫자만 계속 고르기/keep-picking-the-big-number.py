import heapq

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 최대힙을 만들어야하기 때문에 음수로 변경해준다.
nums = [-num for num in nums]
heapq.heapify(nums)

for _ in range(m):
    max_num = heapq.heappop(nums)
    max_num += 1
    heapq.heappush(nums, max_num)

# 나머지 수에서 최대값을 출력한다.
answer = heapq.heappop(nums)
print(-answer)