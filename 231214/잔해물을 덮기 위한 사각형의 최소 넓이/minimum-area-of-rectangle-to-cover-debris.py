OFFSET = 1000
MAX_R = 2000

checked = [ [0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for idx in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    #x1, y1 = x1 + OFFSET, y1 + OFFSET
    #x2, y2 = x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j] = idx + 1

min_row, min_col = MAX_R, MAX_R
max_row, max_col = 0, 0
for r in range(MAX_R + 1):
    for c in range(MAX_R + 1):  
        if checked[r][c] == 1:
            min_row = min(min_row, r)
            max_row = max(max_row, r)

            min_col = min(min_col, c)
            max_col = max(max_col, c)

result = (max_row - min_row + 1) * (max_col - min_col + 1)
print(result)