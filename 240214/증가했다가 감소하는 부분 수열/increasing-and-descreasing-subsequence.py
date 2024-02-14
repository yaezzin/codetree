n = int(input())
nums = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n)] # (최대 증가, 최소 증가) 

for i in range(n):
    dp[0][0] = 1
    dp[0][1] = 1
    
    # 증가하는 부분 수열
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i][0] = max(dp[i][0] , dp[j][0] + 1)

    # 감소하는 부분 수열
    for j in range(i):
        if nums[j] > nums[i]:
            dp[i][1] = max(dp[i][1] , dp[j][1] + 1)

    # 증가하던 것을 멈추고, 감소하는것으로 방향을 옮기는 경우
    dp[i][1] = max(dp[i][1], dp [i][0])

answer = 0
for i in range(n):
    for j in range(2):
        answer = max(answer, dp[i][j])

print(answer)