import sys

n = int(input())
lst = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(n):
    lst[i] *= 2

    
    
    for j in range(n):
        tmp = []
        for k in range(n):
            if j != k:
                # 하나 제외하고 리스트에 넣기
                tmp.append(lst[k])
            
        # 차이구하기
        diff = 0
        for l in range(len(tmp)-1):
            diff += abs(tmp[l] - tmp[l+1])
        
        # 최소값 찾기
        min_diff = min(diff, min_diff)


    # 되돌리기
    lst[i] //= 2

print(min_diff)