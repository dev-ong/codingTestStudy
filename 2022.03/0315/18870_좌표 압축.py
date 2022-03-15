n = int(input())

arr = list(map(int, input().split()))

arr2 = set(arr)

temp = sorted(arr2)

dic = {temp[i]:i for i in range (len(temp))}

for num in arr:
    print(dic[num], end=' ')