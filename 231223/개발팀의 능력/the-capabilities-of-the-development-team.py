import sys

lst = list(map(int, input().split()))

total = sum(lst)

min_diff = sys.maxsize
flag = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i == j or i == k or j == k:
                continue
                
            one = lst[i]
            two = lst[j] + lst[k]
            three = total - one - two

            if one != two and two != three and three != one:

                max_value = max(one, two, three)
                min_value = min(one, two, three)

                min_diff = min(min_diff, max_value - min_value)
                flag = 1

if flag == 0:
    print(-1)
else:
    print(min_diff)