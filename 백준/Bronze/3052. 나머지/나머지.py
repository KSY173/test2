import sys
input = sys.stdin.readline

arr1 = []
arr2 = []
for _ in range(10):
    num = int(input())
    arr1.append(num)
for i in range(10):
    rem = arr1[i] % 42
    arr2.append(rem)
nums = set(arr2)
print(len(nums))