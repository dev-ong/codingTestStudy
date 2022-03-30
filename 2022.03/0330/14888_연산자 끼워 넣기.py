n = int(input())
arr = list(map(int, input().split()))
sig = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def find(depth, total, plus, minus, multi, div):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:
        find(depth + 1, total + arr[depth], plus-1, minus, multi, div)
    if minus:
        find(depth + 1, total - arr[depth], plus, minus-1, multi, div)
    if multi:
        find(depth + 1, total * arr[depth], plus, minus, multi-1, div)
    if div:
        find(depth + 1, int(total / arr[depth]), plus, minus, multi, div-1)


find(1, arr[0], sig[0], sig[1], sig[2], sig[3])
print(maximum)
print(minimum)