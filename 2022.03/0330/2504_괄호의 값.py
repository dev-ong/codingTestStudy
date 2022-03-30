inp = input()

stack = []
tmp = 1
res = 0

for i in range(len(inp)):
    if inp[i] == '(':
        tmp *= 2
        stack.append(inp[i])
    elif inp[i] == '[':
        tmp *= 3
        stack.append(inp[i])
    elif inp[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if inp[i-1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()

    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if inp[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop()

if stack:
    res = 0

print(res)
