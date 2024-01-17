# 입력
n = int(input())

# 상대방 카드 입력
opp_cards = []
for _ in range(n):
    opp_cards.append(int(input()))

b_set = set(opp_cards)

# 내 카드
my_cards = [i for i in range(1, 2 * n + 1) if i not in b_set]

opp_cards.sort()
my_cards.sort()

# 정답 구하기
answer = 0
b_idx = 0
for i in range(n):
    if b_idx < n and my_cards[i] > opp_cards[b_idx]:
        answer += 1
        b_idx += 1
       
print(answer)