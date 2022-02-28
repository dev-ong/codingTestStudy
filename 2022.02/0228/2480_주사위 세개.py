dice = [0] * 7

sol = 0

a, b, c = map(int, input().split())

dice[a] += 1
dice[b] += 1
dice[c] += 1

if max(dice) == 3:
    sol = 10000 + 1000 * dice.index(3)
elif max(dice) == 2:
    sol = 1000 + 100 * dice.index(2)
else:
    temp = []
    for i in range(7):
        if dice[i] == 1:
            temp.append(i)
    sol = max(temp) * 100

print(sol)

