import sys

N = int(sys.stdin.readline())
num = int(sys.stdin.readline())

ans = [[0] * N for _ in range(N)]
ans2 = [0, 0]

# 하 우 상 좌
r, c = 0, 0
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
d = 0

# 달팽이 그리기
val = N * N
while val >= 1:
    if val == num:
        ans2 = [r, c]
    ans[r][c] = val
    nextR = r + dr[d % 4]
    nextC = c + dc[d % 4]
    if (nextR < 0 or nextR >= N or nextC < 0 or nextC >= N) or ans[nextR][nextC] != 0:
        d += 1
    r += dr[d % 4]
    c += dc[d % 4]
    val -= 1

for a in ans:
    print(*a)

print(ans2[0]+1, ans2[1]+1)