n = int(input())
lst = list(map(int, input().split()))

answer = [0] * (n + 1)

numbers = []
for idx, num in enumerate(lst, start=1):
    numbers.append((idx, num))

numbers.sort(key=lambda x: (x[1], x[0]))

for i, (idx, number) in enumerate(numbers):
    answer[idx] = i + 1

for i in range(1, n+1):
    print(answer[i], end =' ')