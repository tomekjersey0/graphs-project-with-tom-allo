import graph
from collections import deque
from typing import Any

# return list of nodes in visitation order

def bfs(g: graph.GRAPH_LIST, start: str) -> list[str]:
    g.clean_graph()

    if not g.find_vertex(start):
        return []

    visited: dict[str, Any] = {}
    q = deque([start])

    while q:
        cur = q.popleft()
        if cur not in visited:
            visited[cur] = None
            for n in g.graph.get(cur, {}):
                if n not in visited:
                    q.append(n)
    
    return list(visited)
    


# return list of nodes in visitation order
def dfs(g: graph.GRAPH_LIST, start: str) -> list[str]:
    return []