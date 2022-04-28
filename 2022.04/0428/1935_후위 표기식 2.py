n = int(input())
s = input()
arr = []
for _ in range(n):
    arr.append(int(input()))
ss = []
for sss in s:
    ss.append(sss)

sigs = ['+', '-', '*', '/']
nums = []
sig = []

# print(ord('A'), ord('Z')) # 65, 90

while len(ss) > 0:
    if ss[0] not in sigs:
        nums.append(arr[ord(ss[0])-65])
        ss.pop(0)
    elif ss[0] == '+':
        n1 = nums[-1]
        n2 = nums[-2]
        nums.pop(-2)
        nums.pop(-1)
        tmp = n1 + n2
        nums.append(tmp)
        ss.pop(0)
    elif ss[0] == '-':
        n1 = nums[-1]
        n2 = nums[-2]
        nums.pop(-2)
        nums.pop(-1)
        tmp = n2 - n1
        nums.append(tmp)
        ss.pop(0)
    elif ss[0] == '/':
        n1 = nums[-1]
        n2 = nums[-2]
        nums.pop(-2)
        nums.pop(-1)
        tmp = n2 / n1
        nums.append(tmp)
        ss.pop(0)
    else:
        n1 = nums[-1]
        n2 = nums[-2]
        nums.pop(-2)
        nums.pop(-1)
        tmp = n1 * n2
        nums.append(tmp)
        ss.pop(0)

print("{:.2f}".format(nums[0]))
