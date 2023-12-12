n = int(input())
lst1 = sorted(list(map(int, input().split())))
lst2 = sorted(list(map(int, input().split())))

if lst1 == lst2:
    print('Yes')
else:
    print('No')