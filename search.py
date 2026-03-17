import graph
import queue



# return list of nodes in visitation order

def bfs(g: graph.GRAPH_LIST, start: str) -> list[str]:
    order: dict[str] = {}

    cur_node = start
    q = queue.Queue(maxsize=0)
    q.put(cur_node)
    while not q.empty():
        cur_node = q.get()
        order.append(cur_node)
        for n in g.graph[cur_node]:
            q.put(n)
        
        
    



# return list of nodes in visitation order
def dfs(g: graph.GRAPH_LIST, start: str) -> list[str]:
    pass