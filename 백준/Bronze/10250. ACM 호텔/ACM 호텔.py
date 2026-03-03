import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    a = (N - 1) // H + 1   # 호수
    b = (N - 1) % H + 1    # 층
    
    print(100 * b + a)