from collections import deque

n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

s = 0
while len(lst) > 1:
    first = lst.pop()
    second = lst.pop()

    s += (first + second)
    lst.append(first + second)

    lst.sort(reverse = True)
    

print(s)