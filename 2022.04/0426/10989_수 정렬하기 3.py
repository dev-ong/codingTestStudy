import sys
input = sys.stdin.readline

n = int(input())

temp = [0] * 10001

for _ in range(n):
    temp[int(input())] += 1

for i in range(10001):
    if temp[i] != 0:
        for j in range(temp[i]):
            print(i)
