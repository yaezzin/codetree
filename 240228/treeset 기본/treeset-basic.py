from sortedcontainers import SortedSet

n = int(input())
ts = SortedSet()

for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation == 'add':
        value = int(command[1])
        
        if value not in ts:
            ts.add(value)
    
    elif operation == 'remove':
        value = int(command[1])
        ts.remove(value)
    
    elif operation == 'find':
        value = int(command[1])
        
        if value in ts:
            print('true')    
        else:
            print('false')

    elif operation == 'lower_bound':
        value = int(command[1])
        idx = ts.bisect_left(value)
        
        if idx < len(ts):
            print(ts[idx])
        else:
            print('None')

    elif operation == 'upper_bound':
        value = int(command[1])
        idx = ts.bisect_right(value)
        
        if idx < len(ts):
            print(ts[idx])
        else:
            print('None')
            
    elif operation == 'largest':
        if ts:
            print(ts[-1])  
        else:
            print('None')  
    
    elif operation == 'smallest':
        if ts:
            print(ts[0])  
        else:
            print('None')