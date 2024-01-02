from itertools import combinations

def is_equal(a, b, c, d, sum_lst):
    #tmp = [ a, b, c, d,
    #        a + b, b + c, c + d, d + a, a + c, b + d, 
    #        a + b + c, a + b + d, a + c + d, b + c + d, a + b + c + d] 

    comb = []
    for r in range(1, len(sum_lst) + 1):
        comb.extend(combinations([a, b, c, d], r))
    
    s = []
    for c in comb:
        s.append(sum(c))
    
    sum_lst.sort()
    s.sort()

    if sum_lst == s:
        return True
    
    return False


lst = list(map(int, input().split()))
for a in range(1, 41):
    for b in range(a, 41):
        for c in range(b, 41):
            for d in range(c, 41):
                if is_equal(a, b, c, d, lst):
                    print(a, b, c, d)
                    #exit()