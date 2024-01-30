import sys

sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parent = [-1] * (N+1)

for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def dfs(current, graph, visited, parentNode):
    visited[current] = True
    parent[current] = parentNode
    for adj in graph[current]:
        if not visited[adj]:
            dfs(adj, graph, visited, current)

dfs(1, graph, visited, -1)

for p in parent[2:]:
    print(p)