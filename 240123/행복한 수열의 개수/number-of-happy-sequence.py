def find_happy(n, m):
    total = 0
    
    # row 확인하기
    for i in range(n):
        row_count = 1
        flag = 0
        for j in range(1, n):
            if grid[i][j-1] == grid[i][j]:
                row_count += 1

            else:
                row_count = 1
            
            if row_count >= m:
                    flag = 1
                    
        if flag:
            total += 1


    # col 확인하기
    for i in range(n):
        col_count = 1
        flag1 = 0
        for j in range(1, n):
            if grid[j-1][i] == grid[j][i]:
                col_count += 1
            
            else:
                col_count = 1

            if col_count >= m:
                    flag1 = 1
        
        if flag1:
            total += 1
    
            
    return total

n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

result = find_happy(n, m)
print(result)