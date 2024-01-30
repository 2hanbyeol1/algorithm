import sys

def solution(n, wires):    
    answer = sys.maxsize
    for wire_idx in range(len(wires)): # 끊어진 와이어의 index
        new_wires = wires.copy()
        new_wires.pop(wire_idx)
        visited = [False] * (n+1)
        dfs(1, new_wires, visited)
        count = 0
        for v in visited:
            if v: count += 1
        gap = abs(n - 2 * count)
        if gap < answer: answer = gap
        print(wires[wire_idx], visited, count, gap)
    return answer

def dfs(n, wires, visited):
    visited[n] = True
    for wire in wires:
        if wire[0] == n and not visited[wire[1]]:
            dfs(wire[1], wires, visited)
        if wire[1] == n and not visited[wire[0]]:
            dfs(wire[0], wires, visited)
    # for wire