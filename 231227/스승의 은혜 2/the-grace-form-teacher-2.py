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
        if prefix_sum <= budget:
            prefix_sum += p[j]
            cnt += 1
  
    p[i] *= 2
    max_student = max(max_student, cnt-1)

print(max_student)