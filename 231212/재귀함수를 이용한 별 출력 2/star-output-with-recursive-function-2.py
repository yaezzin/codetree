def print_star(n):
    if n == 0:
        return
    
    print('* ' * n)
    print_star(n-1)
    print('* ' * n)


n = int(input())
print_star(n)