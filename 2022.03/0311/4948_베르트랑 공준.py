
def find(x):
    if x == 1:
        return False
    for j in range(2, int((2 * i) ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

while True:
    n = int(input())
    sol = 0
    if n == 0:
        break
    for i in range(n, 2*n+1):
        if find(i):
            sol += 1

    print(sol)


