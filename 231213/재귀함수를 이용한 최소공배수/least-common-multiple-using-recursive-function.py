def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm_recursive(x, y):
    gcd = find_gcd(x, y)
    return x * y // gcd

def find_lcm_recursive_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return find_lcm_recursive(numbers[0], find_lcm_recursive_list(numbers[1:]))


n = int(input())
numbers = list(map(int, input().split()))
lcm_result = find_lcm_recursive_list(numbers)
print(lcm_result)