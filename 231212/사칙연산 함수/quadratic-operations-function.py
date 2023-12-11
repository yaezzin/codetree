def func(a, command, b):
    a = int(a)
    b = int(b)

    if command == '*':
        return a * b
    
    elif command == '+':
        return a + b
    
    elif command == '-':
        return a - b

    elif command == '/':
        return a // b

    else:
        return -1


a, command, b = input().split()
tmp = func(a, command, b)

if tmp != -1:
    print(a, command, b, '=', tmp)
else:
    print('False')