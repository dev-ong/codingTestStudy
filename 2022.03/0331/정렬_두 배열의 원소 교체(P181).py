import sys
sys.stdin = open('input.txt')


n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


while k > 0:
    A.sort()
    B.sort()
    small = A[0]
    A.pop(0)
    big = B[-1]
    B.pop(-1)
    A.append(big)
    B.append(small)
    k -= 1


print(sum(A))