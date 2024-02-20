n, m = map(int, input().split())

dic = {}
for i in range(1, n + 1):
    s = input()

    dic[s] = i
    dic[str(i)] = s


for _ in range(m):
    q = input()
    print(dic[q])