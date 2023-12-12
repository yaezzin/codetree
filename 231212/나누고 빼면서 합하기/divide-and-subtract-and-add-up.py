n, m = map(int, input().split())
lst = list(map(int, input().split()))

def get_answer():
    # m을 가져와서 사용하기 위해서 global 붙여주기
    global m

    s = 0
    while m >= 1:
        
        s += lst[m - 1]

        if m % 2 == 0:
            m //= 2
        
        else:
            m -= 1

    return s

print(get_answer())