def solution(progresses, speeds):
    # answer = []
    # return answer

    ans = []

    while len(progresses) >= 1:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
            if len(progresses) == 0:
                break
        if cnt != 0:
            ans.append(cnt)
    return ans

print(solution([93, 30, 55], [1, 30, 5]))

