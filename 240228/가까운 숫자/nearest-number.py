import sys

from sortedcontainers import SortedSet

n = int(input())
nums = list(map(int, input().split()))

ts = SortedSet([0])

for num in nums:
    # 값을 하나씩 넣어준다
    ts.add(num)
    
    answer = sys.maxsize
    for i in range(len(ts) - 1):
        right_idx = ts.bisect_right(ts[i])
        answer = min(answer, ts[right_idx] - ts[i])
    
    print(answer)