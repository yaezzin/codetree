from sortedcontainers import SortedSet 

ts = SortedSet()

n = int(input())
for _ in range(n):
    P, L = map(int, input().split())
    ts.add((L, P)) # (난이도, 번호순으로 넣기)

m = int(input())
for _ in range(m):
    command = input().split()
    operation = command[0]
    
    if operation == 'rc':
        x = int(command[1])
        print(ts[-1][1] if x == 1 else ts[0][1])
    
    elif operation == 'ad':
        P, L = int(command[1]), int(command[2])
        ts.add((L, P))
    
    else:
        P, L = int(command[1]), int(command[2])
        ts.remove((L, P))