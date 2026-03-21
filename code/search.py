import graph
from collections import deque
from typing import Any

# return list of vertices in visitation order

def bfs(g: graph.GraphList, start: str) -> list[str]:
    if not g.find_vertex(start):
        return []

    # Using a dictionary instead of a set to preserve visitation order
    # (Python dicts maintain insertion order)
    visited: dict[str, Any] = {start: None}
    q = deque([start])

    while q:
        cur = q.popleft()
        for n in g.graph.get(cur, {}):
            if n not in visited:
                visited[n] = None
                q.append(n)
    
    return list(visited)
    


# return list of vertices in visitation order
def dfs(g: graph.GraphList, start: str) -> list[str]:
    if not g.find_vertex(start):
        return []
    
    visited = {}

    def explore(current_vertex):
        visited[current_vertex] = None

        for n in g.graph.get(current_vertex, {}):
            if n not in visited:
                explore(n)
    
    explore(start)
    return list(visited.keys())

        