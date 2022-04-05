T = int(input())
for tc in range(1, T + 1):
    m, d, M, D = map(int, input().split())
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def tday(a, b):
        total = 0
        for i in range(a):
            total += day[i]
        total += b
        return total
    result = tday(M, D) - tday(m, d) + 1
    print('#{} {}'.format(tc, result))