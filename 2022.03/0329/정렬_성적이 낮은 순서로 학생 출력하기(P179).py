# import sys
# sys.stdin = open("input.txt")

n = int(input())
arr = []
for _ in range(n):
    name, age = input().split()
    arr.append((name, age))

arr.sort(key=lambda x:x[1])

for i in range(n):
    print(arr[i][0], end=' ')