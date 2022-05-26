T = int(input())

for _ in range(T):
    n = input()
    tmp = ''
    for i in range(len(n)-1, -1, -1):
        tmp += n[i]
    num = int(n) + int(tmp)
    print("YES" if num == num[::-1] else "NO")
