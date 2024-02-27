n = int(input())

s = set()
for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation == 'find':
        x = command[1]
        if x in s:
            print('true')
        else:
            print('false')
    
    elif operation == 'add':
        x = command[1]
        s.add(x)
    
    elif operation == 'remove':
        x = command[1]
        s.remove(x)