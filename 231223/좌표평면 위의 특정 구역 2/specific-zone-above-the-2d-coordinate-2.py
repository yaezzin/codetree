import sys

n = int(input())
points = [ list(map(int, input().split())) for _ in range(n)]

min_area = sys.maxsize

for i in range(n):
    min_x = sys.maxsize
    min_y = sys.maxsize
    
    max_x = 0
    max_y = 0

    for j in range(n):
        if i == j:
            continue
        
        min_x = min(min_x, points[j][0])
        min_y = min(min_y, points[j][1])

        max_x = max(max_x, points[j][0])
        max_y = max(max_y, points[j][1])
        

    area = (max_x - min_x) * (max_y - min_y)    
    min_area = min(min_area, area)

print(min_area)