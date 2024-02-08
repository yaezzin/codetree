n, m = map(int, input().split())

ws, vs = [], []
for _ in range(n): 
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

dp = [0] * (m + 1)
for i in range(1, m + 1): 
    for j in range(1, n): 
        if i >= ws[j]:
            dp[i] = max(dp[i], dp[i - ws[j]] + vs[j])

answer = 0
for i in range(m + 1):
    answer = max(answer, dp[i])

print(answer)