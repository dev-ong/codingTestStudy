n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for num in arr2:
    s, e = 0, n - 1
    ans = False

    while s <= e:
        m = (s + e) // 2
        if num == arr1[m]:
            ans = True
            print(1)
            break
        elif num > arr1[m]:
            s = m + 1
        else:
            e = m - 1

    if ans == False:
        print(0)