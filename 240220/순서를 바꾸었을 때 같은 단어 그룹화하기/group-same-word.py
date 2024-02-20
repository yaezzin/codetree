n = int(input())

dic = {}
for _ in range(n):
    s = ''.join(sorted(input()))

    if s in dic:
        dic[s] += 1 
    else:
        dic[s] = 1

print(max(dic.values()))