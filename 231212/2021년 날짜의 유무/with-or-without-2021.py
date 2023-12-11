def is_correct(m, d):
    if m < 13 and d <= last_day(m, d):
        return True
    
    return False

def last_day(m, d):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    
    if m == 2:
        return 28
    
    else:
        return 30



m, d = map(int, input().split())
if is_correct(m, d):
    print('Yes')
else:
    print('No')