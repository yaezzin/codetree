n = int(input())

# 상대방 카드
opp_cards = []
for _ in range(n):
    opp_cards.append(int(input()))

my_cards = [i for i in range(1, 2 * n + 1) if i not in opp_cards]

answer = 0
for oc in opp_cards:

    tmp = [ mc for mc in my_cards if mc > oc]
    
    # 상대방이 낸 숫자보다 큰 수를 가지고 있다면 그 중에 최솟값 내기
    if len(tmp) > 0:
        my_cards.remove(min(tmp))
        answer += 1
     
    # 만약 큰수가 없다면
    else:
        my_cards.remove(min(my_cards))
    
    
print(answer)  


# 질 때에는 가지고 있는 것 중에 최솟값을 내서 지기