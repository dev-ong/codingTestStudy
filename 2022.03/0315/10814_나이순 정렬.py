n = int(input())
arr = []
for _ in range(n):
    age, name = input().split()
    arr.append((int(age), name))

arr.sort(key=lambda x:x[0])

for i in arr:
    print(*i, sep=" ")



    # 3
    # 21 Junkyu
    # 21 Dohyun
    # 20 Sunyoung