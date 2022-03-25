import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visited = [[False]*m for _ in range(n)]

visited[r][c] = True

def turn():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn_time = 0

while True:
    turn()
    nr = r + dr[d]
    nc = c + dc[d]

    if visited[nr][nc] == False and arr[nr][nc] == 0:
        visited[nr][nc] = True
        r = nr
        c = nc
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nr = r - dr[d]
        nc = c - dc[d]
        if arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            break
        turn_time = 0

print(cnt)

