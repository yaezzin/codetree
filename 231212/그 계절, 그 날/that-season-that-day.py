def is_leap_year(y):
    if y % 4 != 0:
        return False
    
    if y % 100 != 0:
        return True
    
    if y % 400 == 0:
        return True
    
    return False

def last_day(y, m):
    if not is_leap_year(y) and m == 2:
        return 28
    
    elif m == 2:
        return 29 
    
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    
    else:
        return 31 

def is_wether(m):
    if m == 12 or m == 1 or m == 2:
        print('Winter')
    
    elif m == 3 or m == 4 or m == 5:
        print('Spring')
    
    elif m == 6 or m == 7 or m == 8:
        print('Fall')
    
    else:
        print('Fall')

def is_correct_day(y, m, d):
    if last_day(y, m) >= d:
        is_wether(m)
    else:
        print('-1')

y, m, d = map(int, input().split())
is_correct_day(y, m, d)