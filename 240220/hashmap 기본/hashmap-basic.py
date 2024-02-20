n = int(input())

dic = {}
for _ in range(n):
    command = list(input().split())

    if command[0] == 'add':
        dic[command[1]] = command[2]

    elif command[0] == 'find':
        if command[1] in dic:
            print(dic[command[1]])
        else:
            print('None')

    elif command[0] == 'remove':
        dic.pop(command[1])