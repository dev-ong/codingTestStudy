# import sys
# sys.stdin = open("input.txt")

code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] \
           for _ in range(2)] for _ in range(2)] \
         for _ in range(2)] for _ in range(2)]
code[0][0][0][1][1][0][1] = 0  # 0
code[0][0][1][1][0][0][1] = 1  # 1
code[0][0][1][0][0][1][1] = 2  # 2
code[0][1][1][1][1][0][1] = 3  # 3
code[0][1][0][0][0][1][1] = 4  # 4
code[0][1][1][0][0][0][1] = 5  # 5
code[0][1][0][1][1][1][1] = 6  # 6
code[0][1][1][1][0][1][1] = 7  # 7
code[0][1][1][0][1][1][1] = 8  # 8
code[0][0][0][1][0][1][1] = 9  # 9


def find_pos(arr):
    for i in range(r):
        for j in range(c-1, -1, -1 ):
            if arr[i][j] == 1:
                return (i, j)

T = int(input())
for tc in range(1, T+1):
    r, c = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(r)]

    # 암호코드의 뒤쪽에서 1를 찾아라
    sx, sy = find_pos(arr)
    # 시작 좌표로 이동
    for i in range(8):
        sy -= 7
    sy += 1
    # 암호블럭 안에서 7개씩 패턴(10)과 비교해서 8개의 암호를 추출
    pwd_code = []  # 암호코드
    for i in range(8):
        pwd_code.append(
            code[arr[sx][sy]][arr[sx][sy+1]][arr[sx][sy+2]][arr[sx][sy+3]][arr[sx][sy+4]][arr[sx][sy+5]][arr[sx][sy+6]]
        )
        sy += 7

    #검증코드
    val_code = (pwd_code[0] + pwd_code[2] + pwd_code[4] + pwd_code[6]) * 3 \
               + pwd_code[1] + pwd_code[3] + pwd_code[5] + pwd_code[7]
    if val_code % 10 == 0:
        print("#{} {}".format(tc, sum(pwd_code)))
    else:
        print("#{} {}".format(tc, 0))