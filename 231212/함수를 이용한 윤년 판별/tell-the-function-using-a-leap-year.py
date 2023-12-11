def is_leap_year(n):
    if n % 4 != 0:
        return False
    
    if n % 100 != 0:
        return True
    
    if n % 400 == 0:
        return True
        
n = int(input())

if is_leap_year(n):
    print("true")
else:
    print("false")