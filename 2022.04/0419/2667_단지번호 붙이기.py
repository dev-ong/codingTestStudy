n = int(input())
arr = []
num = []

for _ in range(n):
    arr.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False
    if arr[r][c] == 1:
        global cnt
        cnt += 1
        arr[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            find(nr, nc)
        return True
    return False

cnt = 0
sol = 0

for i in range(n):
    for j in range(n):
        if find(i, j) == True:
            num.append(cnt)
            sol += 1
            cnt = 0

num.sort()
print(sol)
for i in range(len(num)):
    print(num[i])
