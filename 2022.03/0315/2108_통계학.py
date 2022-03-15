n = int(input())
# 평균, 중앙값, 최빈값, 범위

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr)/n))
print(arr[n//2])

from collections import Counter

c = Counter(arr).most_common(2)
if len(arr) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])

print(max(arr) - min(arr))
