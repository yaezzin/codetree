# 동서남북을 동 남 서 북으로 바꾸기

# L이 주어지면 반시계 방향으로
# R이 주어지면 시계방향으로 방향 전환
# F가 주어지면 바라보고 있는 방향으로 한칸 이동 

lst = list(input())
x, y = 0, 0
current_location = 3 # 현재 북쪽을 보고 있음

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for d in lst:
    flag = current_location
    
    if d == 'L':
        flag = (current_location -1 + 4) % 4
        current_location = flag
        
    elif d == 'R':
        flag = (current_location + 1) % 4
        current_location = flag

    else:
        x += dx[flag]
        y += dy[flag]
    

print(x, y)