A, B, C = map(int, input().split())

max_num = 0
for i in range(C//A + 1):
    for j in range(C//B + 1):
        tmp = (A * i) + (B * j)
        
        if tmp <= C:
            max_num = max(max_num, tmp)

print(max_num)