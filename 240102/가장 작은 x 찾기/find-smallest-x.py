import sys

n = int(input())
lst = [ list(map(int, input().split())) for _ in range(n)]

min_num = sys.maxsize
for x in range(1, 10001): 
    
    flag = 0   
    for y in range(n):
        x *= 2
    
        if x < lst[y][0] or x > lst[y][1]:
            flag = 1
    
    if flag == 0:
        min_num = min(min_num, x // (2 ** n))
    
    
print(min_num)