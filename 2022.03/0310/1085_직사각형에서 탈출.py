x, y, w, h = map(int, input().split())

arr = [x, y, abs(x-w), abs(y-h)]

print(min(arr))