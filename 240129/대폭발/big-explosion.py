n, m, r, c = map(int, input().split())

bombs = set()
bombs.add((r-1, c-1))

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def bomb():
    global bombs

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    
    for t in range(1, m + 1):
        distance = 2 ** (t-1)
        
        new_bombs = set()
        for x, y in bombs:
            for dx, dy in zip(dxs, dys):
                nx = x + (dx * distance)
                ny = y + (dy * distance)
                
                if in_range(nx, ny):
                    new_bombs.add((nx, ny))
        
        bombs = bombs.union(new_bombs)
    
    return bombs

print(len(bomb()))