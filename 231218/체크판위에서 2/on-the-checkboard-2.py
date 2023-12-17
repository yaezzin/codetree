n, m = map(int, input().split())
lst = [ list(input().split(' ')) for _ in range(n) ]

answer = 0
for i in range(1, n-1):   
    for j in range(1, m-1):     
        for k in range(i+1, n): 
            for l in range(j+1, m):
                if lst[0][0] != lst[i][j] and lst[i][j] != lst[k][l] and lst[k][l] != lst[n-1][m-1]:
                    answer += 1

            
print(answer // 2)