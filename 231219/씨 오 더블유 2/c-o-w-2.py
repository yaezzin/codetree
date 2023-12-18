n = int(input())
lst = list(input())

answer = 0
for i in range(n):
    for j in range(i+1, n):

        for k in range(j+1, n):
            if lst[i] == 'C' and lst[j] == 'O' and lst[k] == 'W':
                answer += 1

print(answer)