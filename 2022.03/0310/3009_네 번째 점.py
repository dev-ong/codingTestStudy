x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = [x1, x2, x3]
y = [y1, y2, y3]

xs = 0
ys = 0

for i in range(3):
    if x.count(x[i]) == 1:
        xs = x[i]
    if y.count(y[i]) == 1:
        ys = y[i]




print(xs, ys)