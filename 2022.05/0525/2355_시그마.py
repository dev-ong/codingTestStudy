a, b = map(int, input().split())

min_num = min(a, b)
max_num = max(a, b)

n = max_num - min_num

s = (n * (n + 1)) // 2

print(s + (min_num * (n + 1)))