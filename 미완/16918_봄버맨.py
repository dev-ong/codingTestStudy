r, c, n = map(int, input().split())

arr = [list(input()) for _ in range(r)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
arr2 = [['O'*c] for _ in range(r)]
bomb = []

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'O':
            bomb.append((i, j))

print(bomb)

if n == 0 or n == 1:
    print(arr)
elif n % 2 == 0:
    print(arr2)


# def find(arr, i):
#     if i == 0 or i == 1:
#         return
#     elif i % 2 == 0 and i != 0:
#         arr2 = [['o'*c] for _ in range(n)]
#         arr = arr2
#         return arr
#
# find(arr, 2)

# print(arr)