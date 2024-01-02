n = int(input())
people = list(input())

answer = 0
for i in range(len(people)):
    if people[i] == '0':
        people[i] = '1'
        
        # 사이간의 거리 구하기
        idx = []
        for j in range(len(people)):
            if people[j] == '1':
                idx.append(j)

        length = []
        for k in range(len(idx)-1):
            length.append(idx[k+1] - idx[k])
        
        min_length = min(length)
        
        # 최대값
        answer = max(answer, min_length)

        # 되돌리기
        people[i] = '0'

print(answer)