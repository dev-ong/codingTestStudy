n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

def dfs(r, c):
    if r <= -1 or r >= n or c <= -1 or c >= m:
        return False
    if arr[r][c] == 0:
        arr[c][c] = 1
        dfs(r-1, c)
        dfs(r, c - 1)
        dfs(r+1, c)
        dfs(r, c+1)
        return True
    return False

sol = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            sol += 1

print(sol)