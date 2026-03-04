import sys
input = sys.stdin.readline

S = input().strip()

pos = [-1] * 26

for i, ch in enumerate(S):
    idx = ord(ch) - ord('a')
    if pos[idx] == -1:
        pos[idx] = i

print(*pos)