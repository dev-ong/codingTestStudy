n = int(input())
arr = []
rank = [1] * n

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i] += 1

print(*rank)