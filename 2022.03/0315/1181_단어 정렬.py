n = int(input())

arr = []

for _ in range(n):
    arr.append(input())
arr = set(arr)
arr = list(arr)

words = [[] for _ in range(52)]


for i in arr:
    words[len(i)].append(i)

for i in range(len(words)):
    if len(words[i]) > 0:
        print(*sorted(words[i]), sep='\n')
