n = int(input())
lst = [ list(map(int, input().split())) for _ in range(n)]

new_lst = []
for idx, (x, y) in enumerate(lst, start=1):
    new_lst.append([x, y, idx])

new_lst.sort(key=lambda x: (x[0], -x[1]))

for l in new_lst:
    x, y, idx = l
    print(x, y, idx)