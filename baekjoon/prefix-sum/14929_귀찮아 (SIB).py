import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split())) # x1 = x[0]

sum = 0 # x1 ~ xn

for xi in x:
    sum += xi

ans = 0
# x1 * (x2 + x3 + ... + xn) + x2 * (x3 + ... + xn) + xn-1 * xn
for i in range(0, n):
    sum -= x[i]
    ans += x[i] * sum
print(ans)
