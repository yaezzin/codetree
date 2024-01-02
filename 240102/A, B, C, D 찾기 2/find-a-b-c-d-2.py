def is_equal(a, b, c, d, lst):
    tmp = [a, b, c, d,
            a + b, b + c, c + d, d + a, a + c, b + d, 
            a + b + c, a + b + d, a + c + d, b + c + d, a + b + c + d] 

    if all(value in lst for value in tmp):
        return True
    
    return False

lst = list(map(int, input().split()))
for a in range(1, 41):
    for b in range(a, 41):
        for c in range(b, 41):
            for d in range(c, 41):
                if is_equal(a, b, c, d, lst):
                    print(a, b, c, d)
                    exit()