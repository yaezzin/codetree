binary = list(input())

n = 0
for i in range(len(binary)):
    n = n * 2 + int(binary[i])

print(n)