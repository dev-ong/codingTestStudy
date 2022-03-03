T = int(input())

for tc in range(T):
    arr = list((input()))
    sol = 0
    score = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            score += 1
            sol += score
        else:
            score = 0
    print(sol)