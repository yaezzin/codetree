n = int(input())
lst = list(map(int, input().split()))

new_lst = []
for idx, l in enumerate(lst, start=1):
    new_lst.append([idx, l])

new_lst.sort(key=lambda x:x[1])


new2 = []
for idx, (x, y) in enumerate(new_lst, start=1):
    new2.append([idx, x, y])

new2.sort(key=lambda x : x[1])

for l in new2:
    print(l[0], end = ' ')