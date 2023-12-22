n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

answer = 0
if n < 6:
    for i in range(n):
        for j in range(n-2):
            for k in range(i+1, n):
                for l in range(n-2):
                    first_sum = lst[i][j] + lst[i][j+1] + lst[i][j+2]
                    seccond_sum = lst[k][l] + lst[k][l+1] + lst[k][l+2]
                    answer = max(answer, first_sum + seccond_sum)
else:
    for i in range(n):
        for j in range(n-5):
            first_sum = lst[i][j] + lst[i][j+1] + lst[i][j+2]
            second_sum = lst[i][j+3] + lst[i][j+4] + lst[i][j+5]
            answer = max(answer, first_sum + second_sum)
            
print(answer)