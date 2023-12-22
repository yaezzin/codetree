n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2): 
                if i == k and abs(l-j) < 2: # 두칸 이상 차이 나야함
                    continue
                first_sum = lst[i][j] + lst[i][j+1] + lst[i][j+2]
                seccond_sum = lst[k][l] + lst[k][l+1] + lst[k][l+2]
                answer = max(answer, first_sum + seccond_sum)

print(answer)