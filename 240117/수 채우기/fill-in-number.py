n = int(input())

# 5로 나눌 수 있을 때까지 2를 뺴기

answer = 0
while n > 0:
    if n % 5 != 0:
        n -= 2

    else:
        n -= 5

    answer += 1

if n < 0:
    print(-1)
else:
    print(answer)