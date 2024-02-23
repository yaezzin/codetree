from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    command = list(input().split())
    
    if command[0] == 'add':
        k = int(command[1])
        v = int(command[2])
        sd[k] = v

    elif command[0] == 'find':
        k = int(command[1])

        if k in sd:
            print(sd[k])
        
        else:
            print('None')

    elif command[0] == 'remove':
        k = int(command[1])
        sd.pop(k)
    
    else:
        if not sd:
            print('None')
        
        else:
            for value in sd.values():
                print(value, end = ' ')
            print()