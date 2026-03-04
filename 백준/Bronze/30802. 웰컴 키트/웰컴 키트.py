import sys
input = sys.stdin.readline

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
count = 0

for d in size:
    count += (d + T - 1) // T
    
pens = N // P
numpen = N % P

print(count)
print(pens, numpen)

