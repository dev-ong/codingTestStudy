A = int(input())
B = int(input())
C = int(input())

target = A*B*C

t = list(str(target))

for i in range(10):
    print(t.count(str(i)))