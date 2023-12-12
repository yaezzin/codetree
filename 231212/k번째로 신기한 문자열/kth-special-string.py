n, k, t = input().split()

tmp = []
for _ in range(int(n)):
    s = input()
    
    if s.startswith(t):
        tmp.append(s)
    
tmp.sort()

print(tmp[int(k) - 1])