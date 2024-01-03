def is_contain(num, lst):
    for l in lst:
        if num < l[0] or num > l[1] :
            return False
    return True

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

flag = 0
for i in range(1, 101):
    if is_contain(i, lst):
        flag = 1


if flag == 1:
    print('Yes')
else:
    print('No')