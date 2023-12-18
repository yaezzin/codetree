n = int(input())

lst = [ list(map(int, input().split())) for _ in range(n) ]

new_lst = []
for idx, (x, y) in enumerate(lst, start=1):
    new_lst.append((idx, x, y))


new_lst.sort(key = lambda x : (abs(x[1]) + abs(x[2])))


for l in new_lst:
    print(l[0])