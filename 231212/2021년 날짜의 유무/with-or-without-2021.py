def is_correct_day(m, d):
    if m > 0 and m < 13:

        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d < 32:
                return True
        
        elif m == 2:
            if d < 29:
                return True
        
        else:
            if d < 31:
                return True
        
        return False
    
    return False


m, d = map(int, input().split())
if is_correct_day(m, d):
    print('Yes')
else:
    print('No')