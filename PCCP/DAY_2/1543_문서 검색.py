import sys

str = sys.stdin.readline()
find = sys.stdin.readline().rstrip()
ans = 0

sLen = len(str)
fLen = len(find)

i = 0
while i <= sLen - fLen:
    found = True
    for j, ch in enumerate(find):
        if str[i + j] != ch:
            found = False
            break
    if found:
        ans += 1
        i += fLen
    else:
        i += 1
print(ans)