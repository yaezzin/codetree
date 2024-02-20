n, m = map(int, input().split())
words = [input() for _ in range(n)]

dic = {}
for i in range(n):
    dic[words[i]] = i

for _ in range(m):
    q = input()

    if q.isdigit():
        print(words[int(q) - 1])
    else:
        print(dic[q] + 1)