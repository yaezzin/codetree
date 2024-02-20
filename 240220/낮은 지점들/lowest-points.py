n = int(input())

dic = {}
for _ in range(n):
    x, y = map(int, input().split())

    if x in dic:
        cur_y = dic[x]
        if cur_y > y:
            dic[x] = y
        
    else:
        dic[x] = y 

print(sum(dic.values()))