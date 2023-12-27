x, y = map(int, input().split())

max_sum = 0
for n in range(x, y+1):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10

    max_sum = max(max_sum, s) 

print(max_sum)