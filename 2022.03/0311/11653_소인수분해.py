N = int(input())

if N == 1:
    print('')

n = N

while n > 1:
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n = n // i
            break



