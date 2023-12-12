n, m = map(int, input().split())
lst_a = list(map(int, input().split()))

def get_answer(a1, a2):
    s = 0

    for i in range(a1 - 1, a2):
        s += lst_a[i]
        
    return s 
    
        
for _ in range(m):
    a1, a2 = map(int, input().split()) 
    print(get_answer(a1, a2))