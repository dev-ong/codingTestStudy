T = int(input())

for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visited = [1] + [0] * sum(score)
    score2 = [0]

    for point in score:
        for i in range(len(score2)):
            if visited[point + score2[i]] == 0:
                visited[point + score2[i]] = 1
                score2.append(point + score2[i])

    print('#{} {}'.format(tc, len(score2)))