n, m = map(int, input().split())

sol = []

def find(dep):
    if dep == m:
        for i in sol:
            print(i, end=' ')
        print()
        return
    for i in range(1, n+1):
        if i not in sol:
            sol.append(i)
            find(dep + 1)
            sol.pop()

find(0)