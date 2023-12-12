def print_hello(n):
    if n == 0:
        return
    
    print_hello(n - 1)
    print("HelloWorld")


n = int(input())
print_hello(n)