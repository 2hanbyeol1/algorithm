import sys
str = sys.stdin.readline().rstrip()

# 파이썬
if str == str[::-1]:
    print(1)
else:
    print(0)