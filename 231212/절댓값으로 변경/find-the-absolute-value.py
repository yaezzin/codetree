def change_abs(lst):
    for i in range(len(lst)):
        lst[i] = abs(lst[i])
    
    print(*lst)

n = int(input())
lst = list(map(int, input().split()))
change_abs(lst)