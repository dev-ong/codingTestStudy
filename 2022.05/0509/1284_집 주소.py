while True:
    n = input()
    if n == 0:
        break
    sol = len(n) + 1

    for num in n:
        if num == '0':
            sol += 4
        elif num == '1':
            sol += 2
        else:
            sol += 3
    print(sol)