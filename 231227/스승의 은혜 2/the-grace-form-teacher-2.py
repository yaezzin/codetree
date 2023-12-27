n, budget = map(int, input().split())

p = []
for _ in range(n):
    p.append(int(input()))

p.sort()

max_student = 0
for i in range(n):
    prefix_sum, cnt = 0, 0
    p[i] //= 2

    for j in range(n):
        prefix_sum += p[j]
        if prefix_sum <= budget:
            cnt += 1
        else:
            break
            
    p[i] *= 2
    max_student = max(max_student, cnt)

print(max_student)