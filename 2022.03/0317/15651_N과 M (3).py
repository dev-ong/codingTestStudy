n, m = map(int, input().split())

sol = []

def perm(x):
    if len(sol) == m:
        print(*sol, end=" ")
        print()


    for i in range(1, n+1):
        for j in range(1, n+1):
            sol.append(j)
            perm(x+1)
            sol.pop()

perm(1)
