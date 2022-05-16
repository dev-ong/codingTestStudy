N = int(input())

a = 5
b = 7

for i in range(1, N):
    a += b
    b += 3

print(a % 45678)