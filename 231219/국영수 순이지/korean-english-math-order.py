n = int(input())
lst = [ list(input().split()) for i in range(n)]

lst.sort(key=lambda x : (-int(x[1]), -int(x[2]), -int(x[3])))

for u in lst:
    name, kor, eng, mat = u
    print(name, kor, eng, mat)