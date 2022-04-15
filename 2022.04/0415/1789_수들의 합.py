s = int(input())

n = 0

sol = 0

for i in range(1, s+1):
    sol += i
    n += 1
    if sol > s:
        n -= 1
        break

print(n)