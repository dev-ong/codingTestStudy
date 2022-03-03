arr = []

for _ in range(10):
    n = int(input())
    arr.append(n)

temp = [0] * 42

for i in range(10):
    t = arr[i] % 42
    temp[t] += 1

sol = 0

for i in range(len(temp)):
    if temp[i] != 0:
        sol += 1

print(sol)

