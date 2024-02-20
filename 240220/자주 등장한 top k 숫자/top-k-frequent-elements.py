# 자주 등장한 순서대로 k개 출력 - 횟수가 동일하면 값이 더 큰숫자 먼저 출력
from collections import Counter

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
counts = Counter(nums)

result = sorted(counts.most_common(k), key=lambda x: (-x[1], -x[0]))
for r in result:
    print(r[0], end = ' ')