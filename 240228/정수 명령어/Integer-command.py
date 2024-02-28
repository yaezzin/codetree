from sortedcontainers import SortedSet

t = int(input())
ts = SortedSet()

for _ in range(t):
    k = int(input())

    for _ in range(k):
        command = input().split()
        operation = command[0]
    
        if operation.startswith('I'):
            value = int(command[1])
            ts.add(value)        
    
        elif operation.startswith('D'):
            if not ts:
                continue
            
            value = int(command[1])

            if value == 1:
                ts.remove(ts[-1])
            else:
                ts.remove(ts[0])


    if ts:
        print(ts[-1], ts[0])
    else:
        print('EMPTY')