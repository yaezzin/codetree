import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [INT_MAX] * (m + 1)

def solution():
    dp[0] = 0

    for i in range(1, n):
        for j in range(m, -1, -1): # 거꾸로 돌면서
            if j >= nums[i]:
                dp[j] = min(dp[j], dp[j - nums[i]] + 1)

solution()

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])