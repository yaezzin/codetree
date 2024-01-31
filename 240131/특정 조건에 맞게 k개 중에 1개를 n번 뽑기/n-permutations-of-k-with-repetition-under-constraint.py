k, n = map(int, input().split())
answer = []

def print_num():
    print(*answer)

def choose(cur_num):
    if cur_num == n + 1:
        print_num()
        return
    
    for i in range(1, k + 1):
        if cur_num >= 3 and answer[cur_num - 2] == i and answer[cur_num-3] == i:
            continue
        answer.append(i)
        choose(cur_num + 1)
        answer.pop()

choose(1)