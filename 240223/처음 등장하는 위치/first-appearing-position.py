from sortedcontainers import SortedDict

n = int(input())
nums = list(map(int, input().split()))

sd = SortedDict()

for i in range(len(nums)):
    if nums[i] not in sd:
        sd[nums[i]] = i + 1

for k, v in sd.items():
    print(k, v)