n = int(input())
lst = list(map(int, input().split()))
lst.sort()

start = 0
end = 2 * n - 1
max_value = 0

while start < end:
    tmp = lst[start] + lst[end]
    max_value = max(max_value, tmp)

    start += 1
    end -= 1

print(max_value)