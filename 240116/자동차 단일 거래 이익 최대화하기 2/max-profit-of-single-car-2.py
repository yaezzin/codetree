n = int(input())
lst = list(map(int, input().split()))

max_value = 0
pivot = lst[0]

for i in range(1, len(lst)):
    if pivot <= lst[i]:
        max_value = max(max_value, lst[i] - pivot)
    
    else:
        pivot = lst[i]

print(max_value)