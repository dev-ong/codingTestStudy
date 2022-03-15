n = int(input())

arr = []

for tc in range(n):
    arr.append(int(input()))

arr.sort()

for num in arr:
    print(num)