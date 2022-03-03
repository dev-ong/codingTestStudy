arr = []
for _ in range(9):
    n = int(input())
    arr.append(n)
print(max(arr))
print(arr.index(max(arr)) + 1)