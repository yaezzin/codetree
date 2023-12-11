def find_min(*args):
    return min(args)


a, b, c = map(int, input().split())
print(find_min(a, b, c))