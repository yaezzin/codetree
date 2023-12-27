n, budget = map(int, input().split())

p = []
for _ in range(n):
    p.append(int(input()))

max_student = 0
for i in range(n):
    prefix_sum, cnt = 0, 0

    for j in range(n):
        if i == j:
            p[i] //= 2
        
        prefix_sum += p[j]

        if prefix_sum <= budget:
            cnt += 1
        
    
    p[i] *= 2

          
    max_student = max(max_student, cnt)

print(max_student)