# a ~ b칸까지 각각 블럭을 1씩 쌓으려는 명령이 k번 주어지고 최대값을 구해라

n, k = map(int, input().split())

lst = [ 0 for _ in range(n + 1)]
for _ in range(k):
    s, e = map(int, input().split())
    
    for i in range(s, e + 1):
        lst[i] += 1

print(max(lst))