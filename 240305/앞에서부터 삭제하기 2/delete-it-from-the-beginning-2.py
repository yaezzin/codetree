import heapq

n = int(input())
nums = list(map(int, input().split()))

answer = 0
for k in range(n-1, 1, -1):
    heapq.heapify(nums[k:])
    heapq.heappop(nums)

    avg = sum(nums) / len(nums)
    answer = max(answer, avg)

print("{:.2f}".format(avg))