n = int(input())

cnt = 0
num = 666

while n != 0:
    if '666' in str(num):
        n -= 1
        if n == 0:
            break
    num += 1

print(num)
