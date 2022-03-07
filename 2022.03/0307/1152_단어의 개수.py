s = input()

cnt = 0
sol = 0
for i in s:
    if i == ' ':
        cnt += 1

if s[0] == ' ' and s[-1] == ' ':
    sol = cnt - 1
elif s[0] == ' ':
    sol = cnt
elif s[-1] == ' ':
    sol = cnt
else:
    sol = cnt + 1

print(sol)