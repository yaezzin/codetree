n = int(input())
lst = [ list(map(int, input().split())) for _ in range(n)]

# 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0
for x in range(n):

    for y in range(n):
        cnt = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if lst[nx][ny] == 1:
                    cnt += 1
            
        if cnt >= 3:
            answer += 1

print(answer)