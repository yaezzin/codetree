n = int(input())
lst = list(map(int, input().split()))

tmp = []
for i in range(1, len(lst) + 1):
    tmp.append(lst[i-1])

    if i % 2 != 0:
        tmp.sort()
        print(tmp[len(tmp) // 2], end = ' ')
        


# 1 2 4 5 6 7 9 10 11