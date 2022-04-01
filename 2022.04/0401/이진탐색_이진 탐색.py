def binary_search(arr, target, s, e):
    if s > e:
        return None
    m = (s + e) // 2
    if arr[m] == target:
        return m
    elif arr[m] > target:
        return binary_search(arr, target, s, m -1)
    else:
        return binary_search(arr, m + 1, e)

n, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n -1)

if result == None:
    print("답이 존재하지 않습니다.")
else:
    print(result+1)