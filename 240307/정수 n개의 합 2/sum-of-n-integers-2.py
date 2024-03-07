n, k = map(int, input().split())
nums = [0] + list(map(int, input().split()))

prefix_sum = [0] * len(nums)

for i in range(1, len(nums)) :
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

answer = 0
for i in range(len(nums) - k):
    answer = max(answer, prefix_sum[i+k] - prefix_sum[i])

print(answer)