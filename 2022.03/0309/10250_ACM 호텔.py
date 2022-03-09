T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        y = N // H
        x = H * 100
    else:
        y = N // H + 1
        x = N % H * 100
    print(x+y)