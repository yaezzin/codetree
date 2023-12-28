A, B, C = map(int, input().split())

max_num = 0
for i in range(A):
    for j in range(B):
        tmp = (A * i) + (B * j)
        
        if tmp <= C:
            max_num = max(max_num, tmp)

print(max_num)