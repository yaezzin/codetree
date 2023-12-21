n = int(input())

lst = [ list(map(int, input().split())) for _ in range(n) ]

sorted_lst = []
for idx, (x, y) in enumerate(lst, start=1):
    s = abs(x) + abs(y)
    sorted_lst.append([idx, s])

sorted_lst.sort(key=lambda x : (x[1], x[0]))

for s in sorted_lst:
    print(s[0])