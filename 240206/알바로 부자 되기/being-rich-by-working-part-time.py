n = int(input())

dp = [0] * n 

# 시간 입력
times = []
for i in range(n):
    times.append(list(map(int, input().split())))

# 끝나는 순, 금액순 정렬
times.sort(key=lambda x: (x[1], -x[2]))

def solution(idx):
    if dp[idx] != 0:
        return dp[idx]

    max_sum = 0
    for i in range(idx + 1, len(dp)):
        if times[idx][1] < times[i][0]:
            max_sum = max(max_sum, solution(i) + times[i][2])
    
    dp[idx] = max_sum
    
    return max_sum

answer = 0
for i in range(n):
    answer = max(answer, times[i][2] + solution(i))

print(answer)