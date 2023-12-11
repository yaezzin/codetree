def is_subsequence(lst):
    if lst == lst2:
        return True
    return False


n1, n2 = map(int, input().split())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

flag = 0
for i in range(n1-n2+1):
    lst = lst1[i : i + len(lst2)]
    
    if is_subsequence(lst):
        flag = 1


if flag == 1:
    print('Yes')
else:
    print('No')