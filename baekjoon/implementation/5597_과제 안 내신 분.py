import heapq
import sys

h = []
for _ in range(28):
    n = int(sys.stdin.readline()) # 제출한 학생의 출석번호
    heapq.heappush(h, n)

found = False # 첫번째 미제출 학생 발견 여부

for i in range(1, 31):
    if h: j = heapq.heappop(h)
    if i != j:
        print(i)
        heapq.heappush(h, j)
        if not found:
            found = True
        else:
            break