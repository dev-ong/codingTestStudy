T = int(input())

for _ in range(T):
    s = input()
    n = str(int(s) + int(s[::-1]))
    if n == n[::-1]:
        print("YES")
    else:
        print("NO")