# h, w, x, y = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(h+x)]
#
# sol = [[0] * w for _ in range(h)]
#
# for i in range((h+x)//2):
#     for j in range(w):
#         sol[i][j] = arr[i][j]
#
# if x < h:
#     for i in range(h-x):
#         for j in range(y, w+y):
#             sol[i+x][j-y] = arr[-1][j]
#
# # for k in range(y, w+y):
# #     sol[-1][k-y] = arr[-1][k]
#
# for i in range(h):
#     print(*sol[i])