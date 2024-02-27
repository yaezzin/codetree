n, k = map(int, input().split())
op = [list(map(int, input().split())) for _ in range(k)]

nums = [0] + [i for i in range(1, n + 1)]
answer = [set() for _ in range(n+1)]

for i in range(1, n + 1):
    answer[i].add(i)

for i in range(3 * k):
    shift = op[i % 4]

    # 자리를 서로 바꿔준다.
    nums[shift[1]], nums[shift[0]] = nums[shift[0]], nums[shift[1]]
    
    # nums[shift[0]]은 바뀌는 수 그자체임
    # 그 바뀌는 수가 '어떤 X번째 자리(=shift[1] 그 자체)'에 갈 수 있는지를 넣어줘야함
    answer[nums[shift[0]]].add(shift[1])
    answer[nums[shift[1]]].add(shift[0])

for i in range(1, n + 1):
    print(len(answer[i]))