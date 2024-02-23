#1 2 3 5 6 0

n, k = map(int, input().split())
nums = list(map(int, input().split()))

two_sum = {}
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        s = nums[i] + nums[j]
        
        diff = k - s

        if diff in two_sum:
            answer += two_sum[diff]

        if s in two_sum:
            two_sum[s] += 1
        else:
            two_sum[s] = 1

print(answer)