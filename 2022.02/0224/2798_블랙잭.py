N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

sol = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                sol = max(sol, arr[i] + arr[j] + arr[k])

print(sol)
