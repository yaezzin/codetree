from sortedcontainers import SortedDict

sd = SortedDict()

n = int(input())

for _ in range(n):
    s = input()
    
    if s in sd:
        sd[s] += 1
    else:
        sd[s] = 1

for k, v in sd.items():
    print(k, "{:.4f}".format((v / n) * 100))