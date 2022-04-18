n = int(input())
arr = [list(input()) for _ in range(n)]

def find_max(arr, n):
    tmp = []

    for i in range(n):
        t = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                t += 1
                if j == n-2:
                    if t == n:
                        return t
                    tmp.append(t)
            else:
                if t == n:
                    return t
                tmp.append(t)
                t = 1

    for i in range(n):
        t = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                t += 1
                if j == n-2:
                    if t == n:
                        return t
                    tmp.append(t)
            else:
                if t == n:
                    return t
                tmp.append(t)
                t = 1

    return max(tmp)

ans = 0

for i in range(n):
    for j in range(n):
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = find_max(arr, n)
            if temp > ans:
                ans = temp
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = find_max(arr, n)
            if temp > ans:
                ans = temp
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(ans)



