n = int(input())

users = []
for _ in range(n):
    users.append(tuple(input().split()))

users.sort(key=lambda x: x[0], reverse=True)

name, addr, city = users[0]

print('name', name)
print('addr', addr)
print('city', city)