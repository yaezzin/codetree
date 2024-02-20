ss = list(input())

dic = {}
for s in ss:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

answer = 'None'
for k, v in dic.items():
    if v == 1:
        answer = k
        break

print(answer)