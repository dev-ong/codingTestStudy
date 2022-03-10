while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)

    arr.sort()

    if arr[2]**2 == arr[0] ** 2 + arr[1] ** 2:
        print('right')
    else:
        print('wrong')