n = int(input())

lst = []
for _ in range(n):
    lst.append(input())

lst.sort(key=lambda x : x * 3, reverse=True)

answer = ''
for l in lst:
    answer += l

print(answer)