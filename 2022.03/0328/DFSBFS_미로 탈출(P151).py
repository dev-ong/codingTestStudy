import sys
sys.stdin = open("input.txt")
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = arr[r][c] + 1
                    q.append((nr, nc))
    return arr[n-1][m-1]
# bfs(0, 0)
# print(arr)

print(bfs(0, 0))




