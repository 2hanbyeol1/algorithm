import sys
import heapq

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split()) # A에서 B로 가는 단방향 도로 존재
    graph[A].append(B)

h = []
INF = sys.maxsize
dist = [INF] * (N+1)

# 다익스트라 알고리즘
heapq.heappush(h, (0, X))
dist[X] = 0

while h:
    now_dist, now = heapq.heappop(h)
    if dist[now] < now_dist:
        continue
    for next in graph[now]:
        cost = now_dist + 1
        if cost < dist[next]:
            dist[next] = cost
            heapq.heappush(h, (cost, next))

# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 출력
found = False
for num, d in enumerate(dist):
    if d == K:
        print(num)
        found = True

if not found: print(-1)