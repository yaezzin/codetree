# 문제 이해가 어려운 문제였음
# ta, tb가 각각 주어질텐데, 이때 온도를 하나씩 체크해가면서 모든 ta~tb에 대해 합을 구해주면서 탐색

N, C, G, H = map(int, input().split())

t = []
for i in range(N):
    ta, tb = map(int, input().split())
    t.append([ta, tb])

max_sum = 0
for i in range(1000):
    s = 0
    for j in range(N):
        ta = t[j][0]
        tb = t[j][1]
        
        if i < ta:
            s += C
        
        elif i >= ta and i <= tb:
            s += G
        
        elif i > tb:
            s += H
    
    max_sum = max(max_sum, s)

print(max_sum)