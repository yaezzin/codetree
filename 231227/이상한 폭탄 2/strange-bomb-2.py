n, k = map(int, input().split())

lst = []
for i in range(n):
    lst.append(int(input()))

max_num = 0
for i in range(n):
    pivot = lst[i]
    cnt = 0

    for j in range(i+1, n):
        if lst[j] == pivot and cnt < 3:
            max_num = max(max_num, pivot)
        
        cnt += 1

print(max_num)