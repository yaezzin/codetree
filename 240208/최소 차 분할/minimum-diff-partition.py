import sys

n = int(input())
nums = list(map(int, input().split()))

s = sum(nums)
dp = [False] * (s + 1)
dp[0] = True

# dp[7] = 7을 합으로 만들 수 있는가?
for i in range(len(nums)):
    for j in range(s, -1 , -1):
        if j >= nums[i] and not dp[j-nums[i]]:
            dp[j] = True


answer = sys.maxsize
for i in range(1, s):
    if dp[i]:
        answer = min(answer, abs((s-i) - i))

print(answer)