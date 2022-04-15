s = input()
pattern = input()
pi = [0 for _ in range(len(pattern))]

# KMP 문자열 검색 알고리즘
# https://bowbowbow.tistory.com/6


def getPI(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def KMP(S, pattern):
    getPI(pattern)
    j = 0
    for i in range(len(S)):
        while j > 0 and S[i] != pattern[j]:
            j = pi[j - 1]
        if S[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

if KMP(s, pattern):
    print('1')
else:
    print('0')
