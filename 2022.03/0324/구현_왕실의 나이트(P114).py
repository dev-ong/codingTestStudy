first = input()
r, c = 0, 0
temp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(8):
    if first[0] == temp[i]:
        c = i
r = int(first[1]) - 1

dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

cnt = 0

for i in range(8):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr < 8 and 0 <= nc < 8:
        cnt += 1
print(cnt)
