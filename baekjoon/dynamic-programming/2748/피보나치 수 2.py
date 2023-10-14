# 0 1 1 2 3 5 8
import sys

memo = [0] * 91
memo[0] = 0
memo[1] = 1

def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        if memo[n] == 0:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

n = int(sys.stdin.readline())
print(fibo(n))