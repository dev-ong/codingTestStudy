H, M = map(int, input().split())
C = int(input())

all = H * 60 + M + C

if all >= 1440:
    all -= 1440

h = all // 60
m = all % 60

if h == 24:
    print(h - 24, m)
else:
    print(h, m)