N = int(input())
arr = list(map(int, input().split()))

max_v = max(arr)

for i in range(N):
    arr[i] = arr[i]/max_v*100

sol = sum(arr) / N

print(sol)
