C = int(input())

for tc in range(C):
    arr = list(map(int, input().split()))
    N = arr[0]

    s = sum(arr) - N
    avg = s / N
    up = 0

    for i in range(1, N + 1):
        if arr[i] > avg:
            up += 1

    rate = up/N*100

    print(f'{rate:.3f}%')