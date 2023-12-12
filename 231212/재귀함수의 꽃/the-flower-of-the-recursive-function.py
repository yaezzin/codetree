def print_sth(n):
    if n == 0:
        return

    print(n, end = ' ')
    print_sth(n-1)
    print(n, end = ' ')

n = int(input())
print_sth(n)