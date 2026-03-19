import graph
import queue
from typing import Any

# return list of nodes in visitation order

def bfs(g: graph.GRAPH_LIST, start: str) -> list[str]:
    visited: dict[str, Any] = {}

    cur = start
    q = queue.Queue(maxsize=0)
    q.put(cur)
    while not q.empty():
        cur = q.get()
        if cur not in visited:
            visited[cur] = None
            for n in g.graph[cur]:
                q.put(n)
    
    return list(visited.keys())
    


# return list of nodes in visitation order
def dfs(g: graph.GRAPH_LIST, start: str) -> list[str]:
    return []