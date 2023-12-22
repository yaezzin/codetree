n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

total = 250

def find_range(lst):
    result = []
    for i in range(len(lst)):
        tmp = []
        
        for j in range(2, 0, -1):
            if lst[i] - j < 0:
                tmp.append(lst[i]- j + n )
            else:
                tmp.append(lst[i] - j)
        
        tmp.append(lst[i])
        
        for j in range(1, 3):
            if lst[i] + j > n:
                tmp.append(lst[i] + j - n)
            
            else:
                tmp.append(lst[i] + j)
        
        result.append(tmp)

    return result

result1 = find_range(lst1)
result2 = find_range(lst2)

tmp = 1
for i in range(3):
    tmp *= len(set(result1[i]) & set(result2[i]))


print(total - tmp)