import sys

N = int(sys.stdin.readline())
num = int(sys.stdin.readline())

ans = [[0] * N for _ in range(N)]
ans2 = [0, 0]

# 상 우 하 좌 상
r = N // 2
c = N // 2
dr = [-1, 0, 1, 0, -1]
dc = [0, 1, 0, -1, 0]

# 달팽이 그리기
val = 1
ans[r][c] = val
if val == num:
    ans2 = [r, c]
val += 1

for i in range(3, N+1, 2): # i x i 박스
    for d in range(5):
        iter = i-1
        if d == 0: iter = 1
        elif d == 1: iter = i-2
        for _ in range(iter):
            r += dr[d]
            c += dc[d]
            ans[r][c] = val
            if val == num:
                ans2 = [r, c]
            val += 1

for a in ans:
    print(*a)

print(ans2[0]+1, ans2[1]+1)