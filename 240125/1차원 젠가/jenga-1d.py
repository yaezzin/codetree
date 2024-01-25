n = int(input())
block = [int(input()) for _ in range(n)]
tmp = [0] * n
except_block = [map(int, input().split()) for _ in range(2)]


for ex in except_block:
    start, end = ex
    
    except_lst = [i for i in range(start-1, end)]

    # start ~ end에 해당하는 것들은 tmp 배열에 넣지 않는다
    tmp_i = 0
    for i in range(n):
        if i not in except_lst:
            tmp[tmp_i] = block[i]
            tmp_i += 1
    

    # 복사해서 넣기
    for i in range(n):
        if tmp[i] != 0:
            block[i] = tmp[i]
    
    block = tmp

# 길이 출력
length = [i for i in block if i != 0]
print(len(length))

# 안의 원소 출력
for b in block:    
    if b != 0:
        print(b)