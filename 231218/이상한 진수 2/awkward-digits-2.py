s = list(input())

def decimal(lst):
    s = 0
    for i in range(len(lst)):
        s = (s * 2 + int(lst[i]))
   
    return s

answer = 0
for i in range(len(s)):
    if s[i] == '1':
        s[i] = '0'
        # 2진법을 => 10진법으로 바꾸기
        result = decimal(s)

        # 최대값 구하기
        answer = max(result, answer)
    
        s[i] = '1'
    else:
        s[i] = '1'
        # 2진법을 => 10진법으로 바꾸기
        result = decimal(s)

        # 최대값 구하기
        answer = max(result, answer)
    
        s[i] = '0'


print(answer)