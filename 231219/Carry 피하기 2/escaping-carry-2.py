n = int(input())
lst = [int(input()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            
            first, second, third = lst[i], lst[j], lst[k]
            multiplier, sum_value, tmp = 1, 0, 0

            # 세 수 중에 한 수라도 0 이상인 동안
            while first > 0 or second > 0 or third > 0 and tmp < 10:
                # 10으로 나눈 나머지를 더해서 승수를 곱해준다.
                tmp = ((first % 10) + (second % 10) + (third % 10))
                sum_value += tmp * multiplier
                #print(sum_value)

                # 그 값이 10보다 크면 break
                if tmp >= 10:
                    break
                
                # 그렇지 않으면 10으로 나누어주고 승수도 10을 높인다.
                first //= 10
                second //= 10
                third //= 10
                multiplier *= 10
        
        # carry가 일어나지 않는 경우에만 정답 갱신
            if first == 0 and second == 0 and third == 0:
                answer = max(answer, sum_value)

if answer == 0:
    print(-1)
else:
    print(answer)