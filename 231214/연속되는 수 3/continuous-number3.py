n = int(input())

lst = [ int(input()) for _ in range(n) ]

points = []
for i in range(n):
    if i == 0 or (lst[i] >= 0 and lst[i-1] < 0) or (lst[i] < 0 and lst[i-1] >= 0):
        points.append(i)

max_value = 0
for i in range(len(points) - 1):
    max_value = max(points[i+1] - points[i], max_value)

print(max_value)