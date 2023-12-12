# 짝수를 제외한 합 -> 재귀

def func(n):
    global count 
    
    if n == 1:
        return count

    if n % 2 == 0:
        n //= 2
        count += 1
        
    else:
        n //= 3
        count += 1
        
    return func(n)


count = 0
n = int(input())
print(func(n))