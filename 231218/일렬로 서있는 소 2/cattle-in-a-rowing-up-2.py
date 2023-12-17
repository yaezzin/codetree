n = int(input())
lst = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i] <= lst[j] and lst[j] <= lst[k]:
                answer += 1

print(answer)