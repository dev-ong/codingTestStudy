def find(r, c, ans):
    global sol
    if ans >= sol:
        return
    if r == N - 1 and c == N - 1:
        if ans < sol:
            sol = ans

    visited[r][c] = 1

    dr = [0, 1]
    dc = [1, 0]

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < N and nc >= 0 and nc < N and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            find(nr, nc, ans + arr[nr][nc])
            visited[nr][nc] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sol = 1000000
    visited = [[0] * N for _ in range(N)]
    find(0, 0, arr[0][0])
    print('#{} {}'.format(tc, sol))