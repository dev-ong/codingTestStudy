n, m = map(int, input().split())

sol = []

def perm(x, y):
    if len(sol) == m:
        print(*sol, end=" ")
        print()
        return



    for j in range(y, n+1):
        sol.append(j)
        perm(x+1, j)
        sol.pop()

perm(1, 1)
