H, W = map(int, input().split())
arr = list(map(int, input().split()))

rain = 0

for i in range(1, W - 1):
    max_left = max(arr[:i+1])
    max_right = max(arr[i:])
    MIN = min(max_right, max_left)
    rain += abs(arr[i] - MIN)

print(rain)