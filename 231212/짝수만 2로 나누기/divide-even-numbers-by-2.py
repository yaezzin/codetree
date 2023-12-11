def is_even(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] //= 2  


n = int(input())
lst = list(map(int, input().split()))
is_even(lst)
print(*lst)