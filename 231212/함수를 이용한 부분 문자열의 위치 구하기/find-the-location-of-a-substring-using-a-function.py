a = list(input())
b = list(input())


def func():
    tmp = -1
    
    for i in range(len(a) - len(b) + 1):

        for j in range(len(b)):

            if a[i+j] == b[j]:
                tmp = i + j
        
        if tmp != -1:
            tmp -= len(b) - 1
            
    return tmp

print(func())