T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    sol1 = 0
    sol2 = 100

    for num in arr:
        if num % 2 == 0:
            sol1 += num
            if num < sol2:
                sol2 = num

    print(sol1, sol2)
