import sys

n = int(sys.stdin.readline()) # 컴퓨터의 수
m = int(sys.stdin.readline()) # 연결된 수

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, graph, visited):
    visited[node] = True
    for adj in graph[node]:
        if not visited[adj]: dfs(adj, graph, visited)

dfs(1, graph, visited) # 전파

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
ans = 0
for v in visited[2:]:
    if v: ans += 1
print(ans)