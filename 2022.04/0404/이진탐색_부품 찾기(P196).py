import sys
sys.stdin = open('input.txt')

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

def find(arr, target, s, e):
    while s <= e:
        m = (s + e) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            e = m - 1
        else:
            s = m + 1
        return None

    for i in arr2:
        result = find(arr1, i, 0, n - 1)
        if result != None:
            print('yes', end= ' ')
        else:
            print('no', end=' ')