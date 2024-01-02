n = int(input())
people = list(input())

answer = 0
for i in range(len(people)):
    if people[i] == '0':
        people[i] = '1'
        
        # 사이간의 거리 구하기
        min_length = n
        for j in range(n):
            for k in range(j+1, n):
                if people[j] == '1' and people[k] == '1':
                    min_length = min(min_length, k - j)

        # 최대값
        answer = max(answer, min_length)

        # 되돌리기
        people[i] = '0'

print(answer)