from typing import Any

# Graph

# Adjacency list implementation
class GRAPH_LIST:
    def __init__(self):
        self.graph: dict[str, dict[str, Any]] = {}

    def add_vertex(self, v: str) -> None:
        self.graph.setdefault(v, dict())

    def add_edge(self, a: str, b: str) -> None:
        self.graph.setdefault(a, dict())[b] = None

    def remove_edge(self, a: str, b: str) -> None:
        if a in self.graph:
            del self.graph[a][b]
            if not self.graph[a]:
                del self.graph[a]

    def remove_vertex(self, v: str) -> None:
        if v in self.graph:
            del self.graph[v]

    def find_vertex(self, v: str) -> bool:
        return True if v in self.graph else False
    
    def find_edge(self, a: str, b: str) -> bool:
        return b in self.graph.get(a, {})

    def path_exists_between(self, a: str, b: str) -> bool:
        return True
