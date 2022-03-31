def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i + 1

s = input().split()
n = int(s[0])
target = s[1]

arr = input().split()

print(sequential_search(n, target, arr))