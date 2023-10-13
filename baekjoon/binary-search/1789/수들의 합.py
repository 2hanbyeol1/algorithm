import sys

S = int(sys.stdin.readline()) # 서로 다른 N개의 자연수의 합

sum = 0
i = 0
while sum <= S:
    i += 1
    sum += i

print(i-1)