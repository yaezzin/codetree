n, k = map(int, input().split())

lst = [0] * 101
for _ in range(n):
    cnt, location = map(int, input().split())
    lst[location] += cnt # 같은 위치에 여러 바구니가 놓일 수 있어서 더해주기

max_value = 0
for c in range(k, len(lst)-k):
    cnt = sum(lst[c-k:c+k+1])
    max_value = max(cnt, max_value)

print(max_value)