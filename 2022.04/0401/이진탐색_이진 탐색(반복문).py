def binary_search(arr, target, s, e):
    while s <= e:
        m = (s + e) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            e = m - 1
        else:
            s = m + 1
    return None

n, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n - 1)

if result == None:
    print("답X")
else:
    print(result + 1)