M = int(input())
N = int(input())

arr = []
temp = []

for _ in range(M, N+1):
    arr.append(_)

for i in range(len(arr)):
    cnt = 0
    if arr[i] != 1:
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                cnt += 1
                break
        if cnt == 0:
            temp.append(arr[i])

if len(temp) == 0:
    print(-1)
else:
    print(sum(temp))
    print(min(temp))

