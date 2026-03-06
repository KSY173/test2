import sys
input = sys.stdin.readline

s = input().strip()

for x in range(10):
    total = 0

    for i in range(13):
        if s[i] == '*':
            digit = x
        else:
            digit = int(s[i])

        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    if total % 10 == 0:
        print(x)
        break