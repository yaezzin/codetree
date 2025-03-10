n, m = map(int, input().split())

jews = [[0,0], ]
for _ in range(n): 
    jews.append(list(map(int, input().split())))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1): 
    for j in range(1, m + 1): 
        if j >= jews[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-jews[i][0]] + jews[i][1])
        else:
            dp[i][j] = dp[i-1][j]

answer = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        answer = max(answer, dp[i][j])
    
print(answer)