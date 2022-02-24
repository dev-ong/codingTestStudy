A, B, C = map(int, input().split())

def findBEP(a, b, c):
    if b >= c:
        return -1
    return a // (c - b) + 1

print(findBEP(A, B, C))

