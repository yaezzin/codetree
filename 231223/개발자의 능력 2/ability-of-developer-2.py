import sys

lst = list(map(int, input().split()))
total = sum(lst)
min_value = sys.maxsize

for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            for l in range(len(lst)):
                if i == j or i == k or i == l or j == k or j == l or k == l:
                    continue

                one = lst[i] + lst[j]
                two = lst[k] + lst[l]
                three = total - one - two

                max_group = max(one, two, three)
                min_group = min(one, two, three)
                min_value = min(min_value, max_group - min_group)
    
print(min_value)