def find(i, total_score, total_calo):
    global taste

    if total_calo > L:
        return

    if i >= N:
        if total_score > taste:
            taste = total_score
        return

    # powerset 알고리즘 사용
    find(i + 1, total_score + scoreList[i], total_calo + caloList[i])
    find(i + 1, total_score, total_calo)

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    scoreList = []
    caloList = []

    for _ in range(N):
        score, calo = map(int, input().split())
        scoreList.append(score)
        caloList.append(calo)

    taste = 0

    find(0, 0, 0)

    print('#{} {}'.format(tc, taste))