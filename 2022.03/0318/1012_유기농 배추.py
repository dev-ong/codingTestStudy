import sys
sys.setrecursionlimit(10**6)

T = int(input())

def find(r, c):
    if r < 0 or r >= M or c < 0 or c >= N:
        return False

    if arr[r][c] == 1:
        arr[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            find(nr, nc)
        return True
    return False


for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for _ in range(K):
        i, j = map(int, input().split())
        arr[i][j] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    sol = 0

    for i in range(M):
        for j in range(N):
            if find(i, j):
                sol += 1
    print(sol)


