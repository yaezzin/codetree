def find_gcd(x, y):
    while y:
        x, y = y, x % y
    
    return x

def find_lcm(x, y):
    gcd = find_gcd(x, y)
    
    return x * y // gcd

def find_lcm_recursive_list(numbers):
    if len(numbers) == 2:
        return find_lcm_recursive(numbers[0], numbers[1])
    else:
        return find_lcm_recursive_list([find_lcm_recursive(numbers[0], numbers[1])] + numbers[2:])


n = int(input())
numbers = list(map(int, input().split()))

lcm_result = find_lcm_recursive_list(numbers)
print(lcm_result)