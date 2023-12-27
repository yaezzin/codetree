k, n = map(int, input().split())

lst = []
for i in range(k):
    lst.append(list(map(int, input().split())))
    
dic = {}
for l in lst:
    for i in range(n-1):
        for j in range(i+1, n):
            tmp = l[i] * 10 + l[j]
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
    
answer = 0
for num, cnt in dic.items():
    if cnt == k:
        answer += 1

print(answer)