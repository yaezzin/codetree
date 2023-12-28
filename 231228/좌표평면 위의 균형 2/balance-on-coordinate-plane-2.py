import sys

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

min_value = sys.maxsize
for x in range(0, 101, 2):
    for y in range(0, 101, 2):
        segments = [0] * 4

        for nx, ny in points:
            # 1사분면
            if nx > x and ny > y:
                segments[0] += 1
            
            # 2사분면
            elif nx < x and ny > y:
                segments[1] += 1

            # 3사분면
            elif nx < x and ny < y:
                segments[2] += 1
            
            elif nx > x and ny < y:
                segments[3] += 1
        
        max_point = max(segments)
        min_value = min(min_value, max_point)

print(min_value)