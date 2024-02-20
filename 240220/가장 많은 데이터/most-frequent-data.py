n = int(input())

dic = {}
for _ in range(n):
    data = input()
    
    if data in dic:
        dic[data] += 1
    else:
        dic[data] = 1

print(max(dic.values()))