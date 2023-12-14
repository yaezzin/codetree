n, t = map(int, input().split())
lst = list(map(int, input().split()))

# T보다 큰 수로 이루어진 연속 부분 수열 중 최대 길이

cnt = 0
max_value = 1
for i in range(len(lst)):
    if lst[i] > t:
        cnt += 1

    else:
        cnt = 0
    
    max_value = max(cnt, max_value)

print(max_value)