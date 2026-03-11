import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = list(range(1, N + 1))
result = []
idx = 0

while queue:
    idx = (idx + K - 1) % len(queue)
    result.append(str(queue.pop(idx)))

print("<" + ", ".join(result) + ">")