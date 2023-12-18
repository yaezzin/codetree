n = int(input())
lst = [list(input().split()) for _ in range(n)]

lst.sort(key = lambda x : int(x[1]) + int(x[2]) + int(x[3]))

for l in lst:
    name, kor, eng, mat = l
    print(name, kor, eng, mat)