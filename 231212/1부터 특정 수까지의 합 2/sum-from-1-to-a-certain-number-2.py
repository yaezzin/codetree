def sum_num(n):
    if n == 0:
        return 0
    
    return n  + sum_num(n-1) 

n = int(input())
print(sum_num(n))