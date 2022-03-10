N = int(input())
arr = list(map(int, input().split()))

sol = N

for i in range(N):
    cnt = 0
    if arr[i] == 1:
        sol -= 1
    if arr[i] != 1:
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                sol -= 1
                break


print(sol)