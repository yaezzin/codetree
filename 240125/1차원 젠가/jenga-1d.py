n = int(input())
blocks = [int(input()) for _ in range(n)]

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def print_result():
    length_without_zero = [i for i in blocks if i != 0]
    print(len(length_without_zero))
    for block in blocks:
        if block != 0:
            print(block)

def push(start, end):
    global blocks 

    tmp_blocks = [0] * n    
    except_lst = [i for i in range(start-1, end)]

    # start ~ end에 해당하는 것들은 tmp 배열에 넣지 않는다
    tmp_idx = 0
    for i in range(n):
        if i not in except_lst:
            tmp_blocks[tmp_idx] = blocks[i]
            tmp_idx += 1
    
    # 복사해서 넣기
    for i in range(n):
        if tmp_blocks[i] != 0:
            blocks[i] = tmp_blocks[i]
    
    blocks = tmp_blocks
    #print(blocks)

push(s1, e1)
push(s2, e2)
print_result()