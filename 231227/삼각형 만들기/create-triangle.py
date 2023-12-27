n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

ms = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i == j or j == k or i ==k:
                continue
            
            first = lst[i]
            second = lst[j]
            third = lst[k]
            
            tmp1 = (first[0] * second[1] + second[0] * third[1] + third[0] * first[1])
            tmp2 = (second[0] * first[1] + third[0] * second[1] + first[0] * third[1])
            s = abs(tmp1-tmp2)
            ms = max(ms, s)

print(ms)