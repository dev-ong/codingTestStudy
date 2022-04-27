n = int(input())
arr = list(map(int, input().split()))
arr = [7] + arr
stu = int(input())
stu_list = []

for _ in range(stu):
    a, b = map(int, input().split())
    stu_list.append([a, b])

for i in range(stu):
    if stu_list[i][0] == 1:
        for j in range(1, len(arr)):
            if j % stu_list[i][1] == 0:
                if arr[j] == 1:
                    arr[j] = 0
                else:
                    arr[j] = 1
    else:
        t = stu_list[i][1]
        d = 0
        while True:
            if t - d - 1 > 0 and t + d + 1 <= n:
                if arr[t - d - 1] == arr[t + d + 1]:
                    d += 1
                else:
                    break
            else:
                break
        for j in range(t - d, t + d + 1):
            if arr[j] == 1:
                arr[j] = 0
            else:
                arr[j] = 1

arr.pop(0)

for i in range(0, n, 20):
    print(*arr[i:i + 20])
