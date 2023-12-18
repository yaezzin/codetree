lst = [input().split() for _ in range(5)]

sorted_by_name = sorted(lst, key=lambda x : (x[0]))
print('name')
for n in sorted_by_name:
    name, h, w = n
    print(name, h, w)

print()

sorted_by_height = sorted(lst, key=lambda x : (-float(x[1])))
print('height')
for n in sorted_by_height:
    name, h, w = n
    print(name, h, w)