n = int(input())
lst = list(map(int, input().split()))

sum_lst = []
for i in range(n):

    for j in range(i+2, n):
        sum_lst.append(lst[i] + lst[j])

print(max(sum_lst))