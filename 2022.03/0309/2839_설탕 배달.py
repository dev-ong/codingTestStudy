N = int(input())

sol  = 0

while N >= 0:
    if N % 5 == 0:
        sol += N // 5
        print(sol)
        break
    N -= 3
    sol += 1
else:
    print(-1)