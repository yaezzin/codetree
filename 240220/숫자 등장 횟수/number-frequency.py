n, m = map(int, input().split())
nums = list(map(int, input().split()))
qna = list(map(int, input().split()))

# 딕셔너리 담기
dic = {}
for n in nums:
    if n in dic:
        dic[n] += 1
    
    else:
        dic[n] = 1

# 질의 응답
for q in qna:
    if q in dic:
        print(dic[q], end = ' ') 
    else:
        print(0, end = ' ')