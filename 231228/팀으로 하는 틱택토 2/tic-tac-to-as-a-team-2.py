# 한줄이 2개의 문자로만 이루어진 경우만 승리한 것

def check_horizental(lst, x, y):
    for i in range(3):
        if lst[i][0] in [x, y] and lst[i][1] in [x, y] and lst[i][2] in [x, y]:
            if lst[i][0] == lst[i][1] and lst[i][1] == lst[i][2]:
                return False
            return True
    return False

def check_vertical(lst, x, y):
    for i in range(3):
        if lst[0][i] in [x, y] and lst[1][i] in [x, y] and lst[2][i] in [x, y]:
            if lst[0][i] == lst[1][i] and lst[2][i] == lst[1][i]:
                return False
            return True
    return False

def check_diagonal(lst, x, y):
    if lst[0][0] in [x, y] and lst[1][1] in [x, y] and lst[2][2] in [x, y]:
        if lst[0][0] == lst[1][1] and lst[2][2] == lst[1][1]:
                return False
        return True
    
    if lst[0][2] in [x, y] and lst[1][1] in [x, y] and lst[2][0] in [x, y]:
        if lst[0][2] == lst[1][1] and lst[2][0] == lst[1][1]:
                return False
        return True
    
    return False

num_lst = []
for _ in range(3):
    num_lst.append(list(map(int, input())))


cnt = 0
for x in range(1, 9):
    for y in range(x+1, 10):
        if check_horizental(num_lst, x, y):
            cnt += 1
        
        elif check_vertical(num_lst, x, y):
            cnt += 1
        
        elif check_diagonal(num_lst, x, y):
            cnt += 1
        
print(cnt)