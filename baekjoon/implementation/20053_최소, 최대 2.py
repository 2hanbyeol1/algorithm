import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline()) # 정수의 개수
    arr = list(map(int, sys.stdin.readline().split()))
    print(min(arr), max(arr))