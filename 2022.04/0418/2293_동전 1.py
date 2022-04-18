n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in arr:
    for j in range(i, k+1):
        if j-i > 0:
            dp[j] += dp[j-1]

print(dp[k])


