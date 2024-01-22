def in_range(row, col, n):
    if row >= 0 and col >= 0 and row + 3 <= n and col + 3 <= n:
        return True
    return False
    

def find_coins(row, col):
    count = 0
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if grid[i][j] == 1:
                count += 1
   
    return count


n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

max_value = 0
for i in range(n):
    for j in range(n):
        if in_range(i, j, n):
            result = find_coins(i, j)
            max_value = max(max_value, result)

print(max_value)