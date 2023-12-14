n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

# 변하는 구간의 idx 넣기 
change_point = []
for i in range(len(lst)):
    if i == 0 or lst[i] != lst[i-1]:
        change_point.append(i)

# 거꾸로 뒤집어서 인덱스 간의 거리 계산
change_point = change_point[::-1]

max_value = 0
for i in range(1, len(change_point)):
    tmp = change_point[i-1] - change_point[i]
    max_value = max(tmp, max_value)

# 만약 max_value가 0이라면 모든 리스트가 동일한 숫자로 이루어졌다는 것
if max_value == 0:
    print(len(lst))
else:
    print(max_value)