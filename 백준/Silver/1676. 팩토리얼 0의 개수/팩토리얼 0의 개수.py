import sys
input = sys.stdin.readline

N = int(input().strip())

count = 0

count += N // 5
count += N // 25
count += N // 125

print(count)