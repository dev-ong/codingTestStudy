# print(ord('a'), ord('A')) # 97 65
# print(ord('z'), ord('Z')) # 122 90

arr = [0] * 26
S = input()

for i in range(len(S)):
    if ord(S[i]) > 96:
        arr[ord(S[i]) - 32 - 65] += 1
    else:
        arr[ord(S[i]) - 65] += 1

M = max(arr)
cnt = 0
sol = chr(arr.index(M)+65)

for n in arr:
    if n == M:
        cnt += 1
        if cnt >= 2:
            sol = '?'
            break

print(sol)