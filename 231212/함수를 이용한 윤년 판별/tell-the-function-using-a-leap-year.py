def is_leap_year(n):
    if n % 4 == 0:
        return 'true'
    
    if n % 4 == 0 and n % 100 == 0:
        if n % 400 == 0:
            return 'true'
        return 'false'

    return 'false'

n = int(input())
print(is_leap_year(n))