import sys

lst = list(map(int, input().split()))
total = sum(lst)

min_value = sys.maxsize
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            s1 = lst[i] + lst[j] + lst[k]
            s2 = total - s1

            min_value = min(min_value, abs(s1-s2))

print(min_value)