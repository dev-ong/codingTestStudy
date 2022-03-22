import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_list = []
for i in range(n):
    max_list.append(min(arr[i]))

print(max(max_list))