x, y = map(int, input().split())

cnt = 0
for num in range(x, y+1):
    num_lst = sorted(list(map(int, set(list(str(num))))))
    
    if len(num_lst) == 2 and num_lst[0] != num_lst[1]:
        cnt += 1
    
print(cnt)