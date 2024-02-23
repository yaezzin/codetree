n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = {}
answer= 0
        
for n in nums:
    diff = k - n 

    # 딕셔너리에 diff가 있으면 가능한 모든 쌍의 수를 더해줌
    if diff in count:
        answer += count[diff]
    
    # 현재 숫자의 개수를 하나 증가 시킴
    if n in count:
        count[n] += 1
    else:
        count[n] = 1
 
print(answer)