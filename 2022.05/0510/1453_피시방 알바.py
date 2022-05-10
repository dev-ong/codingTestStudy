n = int(input())
arr = list(map(int, input().split()))

computer = [0] * 101

sol = 0

for customer in arr:
    if computer[customer] == 0:
        computer[customer] += 1
    else:
        sol += 1

print(sol)