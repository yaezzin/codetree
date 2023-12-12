n = int(input())

def print_small_num(n):
    if n == 0:
        return

    print_small_num(n-1)
    print(n, end = ' ')

def print_big_num(n):
    if n == 0:
        return

    print(n, end = ' ')
    print_big_num(n-1)
    

print_small_num(n)
print()
print_big_num(n)