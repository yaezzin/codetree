n, k = map(int, input().split())

lst = [0] * 101
for _ in range(n):
    cnt, location = map(int, input().split())
    lst[location] += cnt # 같은 위치에 여러 바구니가 놓일 수 있어서 더해주기

max_value = 0
for c in range(101): 
    min_range = max(0, c - k)
    max_range = min(101, c + k + 1)
    
    cnt = sum(lst[min_range:max_range])
    
    max_value = max(cnt, max_value)

print(max_value)