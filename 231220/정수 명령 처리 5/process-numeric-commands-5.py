n = int(input())

lst = []
for _ in range(n):
    value = list(input().split())
    op = value[0]

    if op == 'push_back':
        num = int(value[1])
        lst.append(num)
    
    elif op == 'pop_back':
        lst.pop()
    
    elif op == 'get':
        num = int(value[1])
        print(lst[num-1])
    
    elif op == 'size':
        print(len(lst))