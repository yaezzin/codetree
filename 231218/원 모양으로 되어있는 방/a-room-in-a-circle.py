from collections import deque
import sys

# 1번방에서 시작 (0 1 2 3 4)
# 0 * 4 + 1 *7 + 2 * 8 + 3 * 6 + 4 * 4 

# 2번방에서 시작 (4 0 1 2 3)
# 4 * 4 + 0 * 7 + 1 * 8 + 2 * 6 + 3 * 4

# 3번방에서 시작 (3 4 0 1 2)
# 3 * 4 + 4 * 7 + ..

n = int(input())
lst = [ int(input()) for _ in range(n) ]
deq = deque(i for i in range(n))


answer = sys.maxsize
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += deq[j] * lst[j]
    
    deq.appendleft(deq.pop())
    answer = min(tmp, answer)

print(answer)