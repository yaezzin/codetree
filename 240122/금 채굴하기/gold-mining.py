# Main
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def find_coins(x, y, k):
    s = 0

    for i in range(n):
        for j in range(n):
            if abs(x-i) + abs(y-j) <= k:
                s += grid[i][j]       

    return s

# Answer
answer = 0
for k in range(n+1):
    for i in range(n):
        for j in range(n):
            coin_cnt = find_coins(i, j, k)            
            result = coin_cnt * m - (k * k + (k + 1) * (k + 1))
            
            if result >= 0:
                answer = max(answer, coin_cnt)

print(answer)