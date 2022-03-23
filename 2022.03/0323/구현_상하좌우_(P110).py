import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(input().split())

# U D L R 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

r, c = 0, 0

for w in arr:
    if w == 'U':
        nr, nc = r + dr[0], c + dc[0]
    elif w == 'D':
        nr, nc = r + dr[1], c + dc[1]
    elif w == 'L':
        nr, nc = r + dr[2], c + dc[2]
    else:
        nr, nc = r + dr[3], c + dc[3]
    if 0 <= nr < n and 0 <=nc < n:
        r, c= nr, nc

print(r + 1, c + 1)
