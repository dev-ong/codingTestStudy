import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

sol = 0

for num in arr:
    sol += num ** 2

sol = sol % 10

print(sol)