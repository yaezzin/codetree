# Main
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def find_coins(x, y, k):
    dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

    s = grid[x][y]

    for i in range(8):
        dx, dy = dxs[i], dys[i]
        
        # 대각선 방향 이라면 k-1칸수만큼 확인
        if i % 2 != 0:
            for j in range(k-1):
                new_x, new_y = x + (dx * (j + 1)) , y + (dy * (j + 1))

                if in_range(new_x, new_y):                    
                    s += grid[new_x][new_y]
        
        #위아래좌우방향이라면 K 만큼 개수 확인
        elif i % 2 == 0:
            for j in range(k):
                new_x, new_y = x + (dx * (j + 1)), y + (dy * (j + 1))

                if in_range(new_x, new_y):
                    s += grid[new_x][new_y]
    
    return s

# Answer
answer = 0
for k in range(0, n // 2 + 1):
    for i in range(n):
        for j in range(n):
            coin_cnt = find_coins(i, j, k)
            result = coin_cnt * m - (k * k + (k + 1) * (k + 1))
            if result > 0:
                answer = max(answer, coin_cnt)

print(answer)