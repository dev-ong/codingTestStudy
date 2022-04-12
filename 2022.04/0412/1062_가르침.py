N, K = map(int, input().split())
# abcdefghijklmnopqrstuvwxyz
# anta, tica => 3a, 1c, 1i, 1n, 1t => 단어를 최소 5개 이상 배워야 읽을 수 있음
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

ans = 0

base = ['a', 'c', 'i', 'n', 't']
words = []

for _ in range(N):
    words.append(set(input()))

learn = [0] * 26

for c in base:
    learn[ord(c) - ord('a')] = 1

def find(i, cnt):
    global ans

    if cnt == K - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        ans = max(ans, readcnt)
        return

    for i in range(i, 26):
        if not learn[i]:
            learn[i] = True
            find(i, cnt + 1)
            learn[i] = False

find(0, 0)
print(ans)
