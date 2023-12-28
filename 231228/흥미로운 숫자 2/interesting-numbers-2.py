x, y = map(int, input().split())

cnt = 0
for num in range(x, y+1):
    num_lst = list(str(num))
    
    dic = {}
    for n in num_lst:
        if n in dic:
            dic[n] += 1
            
        else:
            dic[n] = 1

    flag = 0
    if len(dic) == 2:
        for n in dic.values():
            if n == 1:
                flag = 1
    
    if flag == 1:
        cnt += 1

print(cnt)