T = int(input())

for tc in range(T):
    R, S = input().split()
    sol = ''
    for i in range(len(S)):
        for j in range(int(R)):
            sol += S[i]
    print(sol)