n, m, k = map(int, input().split())

# k번 이상 벌칙을 받으면 벌금!
lst = [0] * (n + 1)

answer = []
for i in range(m):
    stuent_num = int(input())
    lst[stuent_num] += 1

    if max(lst) >= k:
        answer.append(stuent_num)

if len(answer) == 0:
    print(-1)
else:
    print(answer[0])