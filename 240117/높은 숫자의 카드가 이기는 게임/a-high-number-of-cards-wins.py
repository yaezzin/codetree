import heapq

# 입력
n = int(input())

# 상대방 카드 입력
opp_cards = []
for _ in range(n):
    opp_cards.append(int(input()))

# 내 카드
my_cards = [i for i in range(1, 2 * n + 1) if i not in opp_cards]
heapq.heapify(my_cards)

# 정답 구하기
answer = 0
for opp_card in opp_cards:

    my_card = heapq.heappop(my_cards)

    if opp_card < my_card:
        answer += 1    
    
print(answer)