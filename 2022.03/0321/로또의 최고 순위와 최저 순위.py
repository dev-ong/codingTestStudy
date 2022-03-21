def solution(lottos, win_nums):
    # answer = []
    mins = 0
    maxs = 0
    f = 0
    l = 0
    for n in lottos:
        for w in win_nums:
            if n == w:
                mins += 1
    for n in lottos:
        if n == 0:
            maxs += 1
    if maxs + mins == 6:
        f = 1
    elif maxs + mins == 5:
        f = 2
    elif maxs + mins == 4:
        f = 3
    elif maxs + mins == 3:
        f = 4
    elif maxs + mins == 2:
        f = 5
    else:
        f = 6
    if mins == 6:
        l = 1
    elif mins == 5:
        l = 2
    elif mins == 4:
        l = 3
    elif mins == 3:
        l = 4
    elif mins == 2:
        l = 5
    else:
        l = 6
    return [f, l]