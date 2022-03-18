n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0
result = 0
sol = []

def find(r, c):
    global cnt

    if r < 0 or r >= n or c < 0 or c >= n:
        return False

    if arr[r][c] == 1:
        cnt += 1
        arr[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            find(nr, nc)
        return True
    return False

for i in range(n):
    for j in range(n):
        if find(i, j) == True:
            sol.append(cnt)
            result += 1
            cnt = 0

sol.sort()
print(result)
for i in range(len(sol)):
    print(sol[i])
