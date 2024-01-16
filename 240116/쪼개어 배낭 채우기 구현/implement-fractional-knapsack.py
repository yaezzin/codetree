n, m = map(int, input().split())

jew = []
for _ in range(n):
    w, v = map(int, input().split())
    jew.append([w, v])

jew.sort(lambda x : (x[1] / x[0]), reverse=True)

s = 0
answer_value = 0
answer_weight = 0
for i in range(len(jew)):
    w, v = jew[i]
    tmp = answer_weight + w

    # 만약 전체를 넣어도 된다면 넣기
    if tmp < m:
        answer_value += v
        answer_weight += w
    
    # 전체를 넣으면 m을 넘는다면 쪼개서 넣기
    else:
        while answer_weight < m :
            answer_value += v / w
            answer_weight += 1

print('{:.3f}'.format(round(answer_value, 3)))