n = int(input())
lst = [input() for _ in range(n)]
lst.sort()
print(*lst, sep = '\n')