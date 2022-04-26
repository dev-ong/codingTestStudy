import sys
input = sys.stdin.readline

n = int(input())

temp = []

for i in range(n):
    temp.append(int(input()))

temp.sort()

for num in temp:
    print(num)