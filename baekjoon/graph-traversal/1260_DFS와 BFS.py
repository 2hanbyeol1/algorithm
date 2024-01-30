import sys
from collections import deque

def dfs(node, graph, visited):
    visited[node] = True
    print(node, end=' ')
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj, graph, visited)

def bfs(node, graph, visited):
    q = deque([node])
    visited[node] = True
    while q:
        n = q.popleft()
        print(n, end=' ')
        for adj in graph[n]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(N+1):
    graph[i].sort()

dfs(V, graph, [False] * (N+1))
print()
bfs(V, graph, [False] * (N+1))