a, b = map(int, input().split())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

answer = len(s1 - s2) + len(s2 - s1)
print(answer)