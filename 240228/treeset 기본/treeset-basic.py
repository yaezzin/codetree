from sortedcontainers import SortedSet

n = int(input())
ts = SortedSet()

for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation == 'add':
        value = command[1]
        ts.add(value)
    
    elif operation == 'remove':
        value = command[1]
        ts.remove(value)
    
    elif operation == 'find':
        value = command[1]
        
        if value in ts:
            print('true')
        
        else:
            print('false')

    elif operation == 'lower_bound':
        value = command[1]
        idx = ts.bisect_left(value)
        
        if idx >= len(ts):
            print('None')
        else:
            print(ts[idx])

    elif operation == 'upper_bound':
        value = command[1]
        idx = ts.bisect_right(value)
        
        if idx >= len(ts):
            print('None')
        else:
            print(ts[idx])
    
    elif operation == 'largest':
        if len(ts) == 0:
            print('None')
        else:
            print(ts[-1])
    
    elif operation == 'smallest':
        if len(ts) == 0:
            print('None')
        else:
            print(ts[0])