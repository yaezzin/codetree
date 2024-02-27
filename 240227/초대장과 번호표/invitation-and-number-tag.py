n, g = map(int, input().split())

answer = set()
answer.add(1) # 첫번째 사람은 무조건 초대하기

for _ in range(g):
    inp = list(map(int, input().split()))
    
    # 각 그룹의 인원 수 
    k = inp[0]

    # 나머지 인원
    people = inp[1:]


    cur_k = 0
    for i in range(k):
        # 현재 그룹 내에서 초대된 사람 수 체크
        if people[i] in answer:
            cur_k += 1
    
    for i in range(k):

        if cur_k == k - 1 and people[i] not in answer:
            answer.add(people[i])


print(len(answer))