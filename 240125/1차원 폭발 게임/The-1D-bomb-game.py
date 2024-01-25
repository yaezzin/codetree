def get_consecutive_counts(grid):
    n = len(grid)
    consecutive_counts = [0] * n

    count = 0
    for i in range(n-1, 0, -1):
        if grid[i] == grid[i-1]:
            count += 1
        else:
            count = 0

        consecutive_counts[i] = count 
        
    return consecutive_counts

def can_bomb(consecutive_counts, m):
    return any(count >= m - 1 for count in consecutive_counts)

def bomb(grid, consecutive_counts, m):
    n = len(grid)
    tmp = [0] * n

    for idx, cnt in enumerate(consecutive_counts): 
        if cnt >= m - 1: 
            for j in range(idx-1, idx + cnt):
                tmp[j] = 1

    return [grid[i] for i in range(n) if not tmp[i]]

# 4 ) 메인 함수
def solution():
    n, m = map(int, input().split())
    grid = [int(input()) for _ in range(n)]
    
    while True:
        consecutive_counts = get_consecutive_counts(grid)    
 
        if not can_bomb(consecutive_counts, m):
            break
        
        grid = bomb(grid, consecutive_counts, m)
        
    # 정답 출력
    print(len(grid))
    print(*grid, sep= '\n')

solution()