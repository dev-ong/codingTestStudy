import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
find = [0]

temp = 0
for i in arr:
    temp += i
    find.append(temp)

for _ in range(m):
    s, e = map(int, input().split())
    print(find[e] - find[s-1])

sol = []

# # 시간초과
# for i in range(m):
#     s, e = find[i]
#     cnt = 0
#     for j in range(s-1, e):
#         cnt += arr[j]
#     sol.append(cnt)

