# greedy는 동전 값이 서로 배수 관계일때만 사용한다.

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0
for c in coins:
    answer += k // c
    k %= c

print(answer)