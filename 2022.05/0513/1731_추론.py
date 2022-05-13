N = int(input())

lst = []

for _ in range(N):
    lst.append(int(input()))

if lst[1] - lst[0] == lst[2] - lst[1]:
    d = lst[2] - lst[1]
    print(lst[-1] + d)
elif lst[2] / lst[1] == lst[1] / lst[0]:
    r = int(lst[1] / lst[0])

print(lst[-1] * r)