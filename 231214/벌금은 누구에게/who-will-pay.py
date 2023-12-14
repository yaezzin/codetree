n, m, k = map(int, input().split())

# k번 이상 벌칙을 받으면 벌금!
lst = [0] * (n + 1)

for _ in range(m):
    stuent_num = int(input())
    lst[stuent_num] += 1

answer = -1
for i in range(len(lst)):
    if lst[i] >= k:
        answer = i
        break

print(answer)