N, K, P, T = map(int, input().split())

# t초에 x와 y가 악수를 한 정보를 입력받는다,
time = []
for i in range(T):
    t, x, y = map(int, input().split())
    time.append([t, x, y])

# 시간순으로 오름차순으로 정렬한다.
time.sort(key=lambda x : x[0])

# 처음 감연자의 정보를 딕셔너리에 넣어준다.   
dic = {}
dic[P] = 0

for t in time:
    _, x, y = t
    
    # 만약 x가 감염자 리스트에 있고, x의 악수 횟수가 K번 이하이면
    if x in dic and dic[x] < K:
        dic[x] += 1 
        
        if y in dic:
            dic[y] += 1
        else:
            dic[y] = 0
        
    elif y in dic and dic[y] < K:
        dic[y] += 1 
        
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 0
        
       
for i in range(1, N+ 1 ):
    if i in dic:
        print(1, end='')
    else:
        print(0, end='')