n = int(input())

arr = []

for tc in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(n):
        if arr[j] >= arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

for num in arr:
    print(num)