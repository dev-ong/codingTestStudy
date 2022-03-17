n, m = map(int, input().split())

sol = []

def perm(x):
    if len(sol) == m:
        print(*sol, end=" ")
        print()
        return # 리턴이 없으면 오답!!!!


    for i in range(1, n+1):
        sol.append(i)
        perm(x+1)
        sol.pop()

perm(1)
