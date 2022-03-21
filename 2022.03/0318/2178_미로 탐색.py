n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]
sol = 10000000
visited = [[False] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find(r, c, ans):
    global sol
    if ans >= sol:
        return

    if r == n - 1 and c == m - 1:
        if sol > ans:
            sol = ans

    visited[r][c] = True

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and visited[nr][nc] == False:
            visited[nr][nc] = True
            find(nr, nc, ans + 1)
            visited[nr][nc] = False

find(0, 0, 1)
print(sol)