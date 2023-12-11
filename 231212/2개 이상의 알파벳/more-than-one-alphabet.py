def func(s):
    l = len(set(list(s)))
    if l >= 2:
        print('Yes')
    else:
        print('No')
    
func(input())