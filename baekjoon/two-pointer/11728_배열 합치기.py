import sys

# 배열 A, B의 크기
N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# 배열 A와 B를 합친 후 정렬한 결과를 출력
pA, pB = 0, 0

while pA < N or pB < M:
    if pA >= N:
        print(B[pB], end=' ')
        pB += 1
    elif pB >= M:
        print(A[pA], end=' ')
        pA += 1
    elif A[pA] < B[pB]:
        print(A[pA], end=' ')
        pA += 1
    else:
        print(B[pB], end=' ')
        pB += 1
