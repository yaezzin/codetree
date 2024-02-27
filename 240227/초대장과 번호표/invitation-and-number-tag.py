n, g = map(int, input().split())

answer = set()
for _ in range(g):
    inp = list(map(int, input().split()))
    
    # 각 그룹의 인원 수 
    k = inp[0]

    # 첫번째는 정답에 넣는다.
    cur_k = 1
    answer.add(inp[1])
    
    # 두번쨰 부터는 체크하기
    for i in range(2, k + 1):
        if cur_k == k - 1 and inp[i] not in answer:
            answer.add(inp[i])
        
        elif len(answer) == k - 1 and inp[i] not in answer:
            answer.add(inp[i])

print(len(answer))