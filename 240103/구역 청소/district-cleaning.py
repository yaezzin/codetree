a, b = map(int, input().split())
c, d = map(int, input().split())

def is_intersecting(x1, x2, x3, x4):
    if x2 < x3 or x4 < x1: # 겹치지 않는 경우
        return False 
    else:
        return True


# 겹친다면 제일 큰놈 - 제일 작은 놈하면 전체 구역의 크기가 나옴
if is_intersecting(a, b, c, d):
    print(max(b, d) - min(a, c))
# 겹치지 않는다면 구역 2개 각각 더하기 
else:
    print(b-a + d-c)