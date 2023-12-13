OFFSET = 1000
MAX_R = 2000

n = int(input())

cur = 0
segments = []
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == 'L':
        section_left = cur - distance
        section_right = cur
        cur = cur - distance 
    
    else:
        section_left = cur 
        section_right = cur + distance
        cur = cur + distance
        
    segments.append([section_left, section_right])


checked = [0] * (MAX_R + 1)
for x1, x2 in segments:
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    for i in range(x1, x2):
        checked[i] += 1

cnt = 0
for e in checked:
    if e >= 2:
        cnt += 1

print(cnt)