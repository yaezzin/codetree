def is_correct_num(n):
    div = n // 10
    mod = n % 10
    tmp = div + mod

    if n % 2 == 0 and tmp % 5 == 0:
        print('Yes')
    else:
        print('No')
    

n = int(input())
is_correct_num(n)