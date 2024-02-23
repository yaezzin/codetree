n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = {}

for e in nums:
    if e in count:
        count[e] += 1
    else:
        count[e] = 1

answer = 0
for i in range(n):
    count[nums[i]] -= 1

    for j in range(i):
        diff = k - nums[i] - nums[j]
        
        if diff in count:
            answer += count[diff]

print(answer)