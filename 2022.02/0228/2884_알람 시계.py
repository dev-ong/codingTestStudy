H, M = map(int, input().split())

all = H * 60 + M

if all > 45:
    all -= 45
else:
    all += 1395

h = all // 60
m = all % 60

if h == 24:
    print(h - 24, m)
else:
    print(h, m)
