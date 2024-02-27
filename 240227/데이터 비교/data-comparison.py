n1 = int(input())
lst1 = list(map(int, input().split()))

n2 = int(input())
lst2 = list(map(int, input().split()))

for elem in lst2:
    if elem in lst1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')