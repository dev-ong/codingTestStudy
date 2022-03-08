N = int(input())

pileup = 1
cnt = 1

while N > pileup:
    pileup += 6 * cnt
    cnt += 1
print(cnt)